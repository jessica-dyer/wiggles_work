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

class DeleteConfirmationScreen(GridLayout):
    
    def __init__(self, wiggles_work_app, name, back_screen, delete_action):
        super().__init__(rows=2)
        self.wiggles_work_app = wiggles_work_app
        self.name = name #A string; the name of the thing to be deleted
        self.back_screen = back_screen #A widget; the screen we want to return to if delete is cancelled
        self.delete_action = delete_action #A function; the function that will be called when delete is confirmed
        self.label = Label(text="")
        self.button_container = GridLayout(cols=2)
        self.no_button = Button(text="No")
        self.yes_button = Button(text="Yes")
        self.add_widget(self.label)
        self.label.text = "Are you sure you want to delete " + name + "?"
        self.add_widget(self.button_container)
        self.button_container.add_widget(self.no_button)
        self.button_container.add_widget(self.yes_button)
        self.no_button.bind(on_press=self.on_click_no)

    def on_click_no(self, button):
        self.wiggles_work_app.window.set_view(self.back_screen)