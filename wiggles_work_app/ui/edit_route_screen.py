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
from enum import Enum
from data_structures.data_structures import *
from ui.delete_confirmation_screen import *
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from ui.ascent_list_view import *


class RouteScreenMode(Enum):
    ADD = 1
    EDIT = 2


class EditRouteScreen(BoxLayout):

    def __init__(self, wiggles_work_app, route):
        super().__init__(orientation='vertical')

        if route is None:
            self.mode = RouteScreenMode.ADD
        else:
            self.mode = RouteScreenMode.EDIT
        self.route = route  # If route is 'None' it is an add not an edit
        self.wiggles_work_app = wiggles_work_app
        self.form_field_grid_layout = GridLayout(cols=1,
                                                 size_hint=(1, 30))

        self.name_field = FormField("Route Name:", "")
        self.grade_field = FormField("Grade:", "")
        self.crag_field = FormField("Crag:", "")

        self.add_widget(self.form_field_grid_layout)
        self.form_field_grid_layout.add_widget(self.name_field)
        self.form_field_grid_layout.add_widget(self.grade_field)
        self.form_field_grid_layout.add_widget(self.crag_field)

        self.current_climber = self.wiggles_work_app.data_repository.climbers[0]
        self.ascent_list_view = AscentListView(size_hint=(1, 60))
        self.ascent_list_view.set_climber(self.wiggles_work_app, self.current_climber)
        self.add_widget(self.ascent_list_view)


        self.button_container = GridLayout(cols=3,
                                           size_hint=(1, 10))
        self.save_button = Button(text="Save")
        self.cancel_button = Button(text="Cancel")
        self.delete_button = Button(text="Delete route")

        self.save_button.bind(on_press=self.on_click_save)
        self.cancel_button.bind(on_press=self.on_click_cancel)
        self.delete_button.bind(on_press=self.on_click_delete)
        self.button_container.add_widget(self.cancel_button)

        if self.mode == RouteScreenMode.EDIT:
            self.button_container.add_widget(self.delete_button)
        self.button_container.add_widget(self.save_button)
        self.add_widget(self.button_container)
        if self.route is not None:
            self.name_field.field.text = self.route.name
            self.grade_field.field.text = self.route.grade
            self.crag_field.field.text = self.route.crag

    def on_click_save(self, button):
        route_to_save = self.route
        if self.mode is RouteScreenMode.ADD:
            route_to_save = Route()
        route_to_save.name = self.name_field.field.text
        route_to_save.grade = self.grade_field.field.text
        route_to_save.crag = self.crag_field.field.text

        if self.mode is RouteScreenMode.ADD:
            self.wiggles_work_app.data_repository.add_route(route_to_save)
        else:
            self.wiggles_work_app.data_repository.update_route(route_to_save)
        self.wiggles_work_app.navigate_to_route_list()

    def on_click_cancel(self, button):
        self.wiggles_work_app.navigate_to_route_list()

    def on_click_delete(self, button):
        foo = DeleteConfirmationScreen(self.wiggles_work_app, self.route.name, self, self.on_delete_confirmed)
        self.wiggles_work_app.window.set_view(foo)

    def on_delete_confirmed(self):
        self.wiggles_work_app.data_repository.delete_route(self.route)
        self.wiggles_work_app.navigate_to_route_list()
