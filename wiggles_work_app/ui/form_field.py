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
from kivy.uix.label import Label

class FormField(GridLayout):

    def __init__(self, label_text, value_text):
        super().__init__(cols = 2)
        self.label = Label(text=label_text)
        self.field = TextInput(text=value_text)
        self.add_widget(self.label)
        self.add_widget(self.field)

    # def build(self):
    #     self.add_widget(self.label)
    #     self.add_widget(self.field)
    #     return self
