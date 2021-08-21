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
from kivy.uix.recycleview import RecycleView
from kivy.base import Builder

from ui.edit_route_screen import *
from wiggles_work_app import *
from ui.route_list_row_view import RouteListRowView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.floatlayout import FloatLayout
from ui.wiggles_work_screen import *


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


RouteListRecycleView_in_Kivy_language = '''

RouteListRecycleView:
    data: []
    viewclass: 'RouteListRowView'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True

'''


class RouteListRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(RouteListRecycleView, self).__init__(**kwargs)
        self.wiggles_work_app = None

    def setWigglesWorkApp(self, wiggles_work_app):
        self.wiggles_work_app = wiggles_work_app
        self.refreshData()

    def refreshData(self):
        all_routes = self.wiggles_work_app.data_repository.routes
        # if you want to sort routes for the list view, sort them in here
        self.data = [{'route': r} for r in all_routes]


class RouteListScreen(GridLayout):

    def __init__(self, wiggles_work_app):
        super().__init__(rows=3)
        self.wiggles_work_app = wiggles_work_app
        self.top_level_layout = GridLayout(rows=3)
        self.recycleView = Builder.load_string(RouteListRecycleView_in_Kivy_language)
        self.recycleView.setWigglesWorkApp(self.wiggles_work_app)
        self.top_level_layout.add_widget(self.recycleView)
        self.button_container = modified_bg_color(FloatLayout)(size_hint=(1, .25))
        self.add_button = MDRectangleFlatButton(text='Add route!',
                                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.button_container.add_widget(self.add_button)
        self.add_button.bind(on_press=self.onClick)
        self.top_level_layout.add_widget(self.button_container)
        self.add_widget(self.top_level_layout)

    def onClick(self, button):
        # add_route_screen = EditRouteScreen(self.wiggles_work_app, route=None)
        # self.wiggles_work_app.window.set_view(add_route_screen)
        test_screen = WigglesWorkScreen()
        self.wiggles_work_app.window.set_view(test_screen)

    def refreshList(self):
        self.recycleView.refreshData()
