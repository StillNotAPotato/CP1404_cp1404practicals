from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabels(App):
    """Construct app to display list of names on separate labels."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app from kv file."""
        super().__init__(**kwargs)
        self.list_to_names = {"Bob Brown": "1", " Cat Cyan": "2", "Oren Ochre": "3"}

    def build(self):
        """Build GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')

        for name in self.list_to_names:
            self.root.ids.name_label.text = name
            print(name)






if __name__ == '__main__':
    DynamicLabels().run()
