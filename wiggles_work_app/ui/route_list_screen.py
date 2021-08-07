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

from ui.edit_route_screen import *
from wiggles_work_app import *



class RouteListScreen(GridLayout):

    def __init__(self, wiggles_work_app):
        super().__init__(rows = 3)
        self.wiggles_work_app = wiggles_work_app
        # self.edit_route_view = None
        self.top_level_layout = GridLayout(rows=3)
        self.add_button = Button(text="Add Route!",
                                 font_size="20sp",
                                 background_color=(66 / 255, 135 / 255, 245 / 255, 1),
                                 color=(2, .5, .5, 1),
                                 size=(32, 32),
                                 size_hint=(.2, .2),
                                 pos=(300, 250))
        self.add_button.bind(on_press=self.onClick)
        self.top_level_layout.add_widget(self.add_button)
        self.add_widget(self.top_level_layout)

    def onClick(self, button):
        add_route_screen = EditRouteScreen(self.wiggles_work_app, route=None)
        self.wiggles_work_app.window.set_view(add_route_screen)
