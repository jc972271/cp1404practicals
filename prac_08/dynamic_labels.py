"""
CP1404 Practical 8
Kivy GUI program to convert miles to kilometers
Liam Whiting, IT@JCU
Started 17/11/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

# from kivy.properties import StringProperty

FONT_SIZE = 48
TEXT_COLOUR = (1, 0, 1, 1)


class DynamicLabelsApp(App):
    """ DynamicLabels is a Kivy App for learning how dynamic labels work."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = ["John", "Steve", "Becca", "Kyle"]

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.font_size = FONT_SIZE
            temp_label.color = TEXT_COLOUR
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
