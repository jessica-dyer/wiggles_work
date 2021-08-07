# import kivy module
import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# The GridLayout arranges children in a matrix.
# It takes the available space and
# divides it into columns and rows,
# then adds widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from ui.edit_route_view import *

class WigglesWorkWindow(App):

    def __init__(self, initial_view):
        super().__init__()
        self.current_view = initial_view

    def build(self):
        return self.current_view

    def set_view(self, new_view):
        self.remove_widget(self.current_view)
        self.add_widget(new_view)
        self.current_view = new_view

