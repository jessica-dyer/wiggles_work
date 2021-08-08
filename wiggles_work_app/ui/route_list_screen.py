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

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

KV = '''

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

        #self.viewclass = 'RouteListRowView'
        #self.data = routes

class RouteListScreen(GridLayout):

    def __init__(self, wiggles_work_app):
        super().__init__(rows = 3)
        self.wiggles_work_app = wiggles_work_app
        # self.edit_route_view = None
        self.top_level_layout = GridLayout(rows=3)
        #self.recycleView = RouteListRecycleView(self.wiggles_work_app.data_repository.master_list.routes)
        self.recycleView = Builder.load_string(KV)
        all_routes = self.wiggles_work_app.data_repository.master_list.routes
        self.recycleView.data = [{'route': r} for r in all_routes]
        self.top_level_layout.add_widget(self.recycleView)
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
