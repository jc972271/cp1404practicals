"""
CP1404 Practical 8
Kivy GUI program to convert miles to kilometers
Liam Whiting, IT@JCU
Started 17/11/2024
"""

from kivy.app import App
from kivy.lang import Builder

class ConvertMilesToKilometersApp(App):
    """ ConvertMilesToKilometersApp is a Kivy App for converting miles to kilometers"""
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesToKilometersApp().run()