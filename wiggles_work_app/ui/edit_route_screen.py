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


class EditRouteScreen(GridLayout):

    def __init__(self, wiggles_work_app, route):
        super().__init__(rows=4)
        self.route = route #If route is 'None' it is an add not an edit
        self.wiggles_work_app = wiggles_work_app
        self.name_field = FormField("Route Name:", "")
        self.grade_field = FormField("Grade:", "")
        self.crag_field = FormField("Crag:", "")
        self.add_widget(self.name_field)
        self.add_widget(self.grade_field)
        self.add_widget(self.crag_field)
        self.button_container = GridLayout(cols=2)
        self.save_button = Button(text="Save")
        self.cancel_button = Button(text="Cancel")
        self.save_button.bind(on_press = self.on_click_save)
        self.cancel_button.bind(on_press=self.on_click_cancel)
        self.button_container.add_widget(self.cancel_button)
        self.button_container.add_widget(self.save_button)
        self.add_widget(self.button_container)

    def on_click_save(self, button):
        print("Not implemented yet.")

    def on_click_cancel(self, button):
        self.wiggles_work_app.navigate_to_route_list()


