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


# class in which we are creating the button
class ButtonApp(App):

    def __init__(self):
        super().__init__()
        self.btn = Button(text="Cuddle Me !",
                          font_size="20sp",
                          background_color=(66 / 255, 135 / 255, 245 / 255, 1),
                          color=(2, .5, .5, 1),
                          size=(32, 32),
                          size_hint=(.2, .2),
                          pos=(300, 250))
        self.btn.bind(on_press=self.onClick)
        self.field = TextInput(text="Type here!")

    def onClick(self, something):
        print("Got a click!")
        print(self.field.text)

    def build(self):
        # use a (r, g, b, a) tuple
        # adding GridLayouts in App
        # Defining number of column
        # You can use row as well depends on need
        layout = GridLayout(rows=2)

        layout.add_widget(self.field)
        layout.add_widget(self.btn)
        return layout


# creating the object root for ButtonApp() class
root = ButtonApp()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
root.run()
