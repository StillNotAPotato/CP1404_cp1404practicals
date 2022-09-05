from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    "App to convert miles to km"
    message = StringProperty()
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_update(self):
        """Update output label"""
        result = self.handle_calculation()
        self.root.ids.output_label.text = str(result)
    def handle_calculation(self):
        """Convert miles to km"""
        value = float(self.root.ids.input_label.text)
        result = value * MILES_TO_KM
        return result
        

    def handle_increment(self):
        pass

    def handle_decrement(self):
        pass

ConvertMilesKm().run()
