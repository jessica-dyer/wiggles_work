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
from ui.form_field import *


class EditRouteView(GridLayout):

    def __init__(self):
        super().__init__(rows=4)
        self.name_field = FormField("Name", "")
        self.grade_field = FormField("Grade", "")
        self.crag_field = FormField("Crag", "")
        self.add_widget(self.name_field)
        self.add_widget(self.grade_field)
        self.add_widget(self.crag_field)

    # def build(self):
    #     layout = GridLayout(rows=4)
    #     layout.add_widget(self.name_field)
    #     layout.add_widget(self.grade_field)
    #     layout.add_widget(self.crag_field)
    #     return layout
