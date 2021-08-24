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
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

from ui.edit_route_screen import *


class WigglesWorkWindow(MDApp):

    def __init__(self):
        super().__init__()
        self.container_layout = GridLayout(rows=1)
        self.current_view = None

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.theme_style = "Dark"
        return self.container_layout

    def set_view(self, new_view):
        if self.current_view is not None:
            self.container_layout.remove_widget(self.current_view)
        self.container_layout.add_widget(new_view)
        self.current_view = new_view
