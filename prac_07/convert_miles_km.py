from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    "App to convert miles to km."
    output_km = StringProperty()
    def build(self):
        """Build app from kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_update(self, miles):
        """Update output label"""
        print("update")
        self.output_km = str(miles * MILES_TO_KM)
        #result = self.handle_calculation()
        #self.root.ids.output_label.text = str(result)

    def handle_calculation(self, text):
        """Convert miles to km."""
        miles = self.convert_to_number(text)
        self.handle_update(miles)


    def handle_increment(self, text, change):
        """Update text input if user press up/down."""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float."""
        try:
            return float(text)
        except ValueError:
            return 0.0



ConvertMilesKm().run()
