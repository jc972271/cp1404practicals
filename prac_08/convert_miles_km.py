"""
CP1404 Practical 8
Kivy GUI program to convert miles to kilometers
Liam Whiting, IT@JCU
Started 17/11/2024
"""
from Demos.security.sspi.validate_password import validate
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609344

class ConvertMilesToKilometersApp(App):
    """ ConvertMilesToKilometersApp is a Kivy App for converting miles to kilometers"""
    output_kilometers = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_result(self):
        value = self.validate_miles()
        result = value * MILES_TO_KM
        self.output_kilometers = str(result)

    def handle_increment(self, increment):
        value = self.validate_miles()
        result = value + increment
        self.root.ids.input_miles.text = str(result)

    def validate_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0






ConvertMilesToKilometersApp().run()