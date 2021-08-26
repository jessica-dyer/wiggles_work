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
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton, MDFloatingBottomButton
from kivy.uix.floatlayout import FloatLayout
from ui.wiggles_work_screen import *
from ui.intro_screen import *
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout
from background_color_debugging import *


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


RouteListRecycleView_in_Kivy_language = '''

RouteListRecycleView:
    data: []
    viewclass: 'RouteListRowView'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        padding: dp(10)
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
        self.show_these_routes(all_routes)

    def show_these_routes(self, list_of_routes):
        list_of_routes.sort(key=lambda x: x.name)
        # if you want to sort routes for the list view, sort them in here
        self.data = [{'route': r} for r in list_of_routes]


class RouteListScreen(WigglesWorkScreen):

    def __init__(self, wiggles_work_app):
        super().__init__()
        self.wiggles_work_app = wiggles_work_app
        self.icon = MDIconButton(icon='magnify')
        self.search_field = MDTextField(hint_text='Search routes')
        self.search_field_container = BoxLayout(orientation='horizontal',
                                                spacing=5,
                                                padding=(20, 0, 20, 0),
                                                size_hint_y=None,
                                                height=50)
        self.search_field_container.add_widget(self.icon)
        self.search_field_container.add_widget(self.search_field)
        self.recycleView = Builder.load_string(RouteListRecycleView_in_Kivy_language)
        self.recycleView.setWigglesWorkApp(self.wiggles_work_app)
        # self.add_button = MDFillRoundFlatButton(text='Add route!',
        #                                         pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.add_button = MDFloatingBottomButton(icon='plus-thick')
        self.toolbar.left_action_items = [["arrow-left-bold", lambda x: self.on_click_back()]]
        self.screen_content.add_widget(self.search_field_container)
        self.screen_content.add_widget(self.recycleView)
        self.bottom_button_container.add_widget(self.add_button)

        self.search_field.bind(on_text_validate=self.on_search_text_entered)
        self.add_button.bind(on_press=self.onClick)

    def onClick(self, button):
        add_route_screen = EditRouteScreen(self.wiggles_work_app, route=None)
        self.wiggles_work_app.window.set_view(add_route_screen)

    def on_click_back(self):
        intro_screen = IntroductionScreen(self.wiggles_work_app)
        self.wiggles_work_app.window.set_view(intro_screen)

    def refreshList(self):
        self.recycleView.refreshData()

    def on_search_text_entered(self, other):
        print(self.search_field.text)
        filter_routes = self.wiggles_work_app.data_repository.getRoutesMatching(self.search_field.text)
        self.recycleView.show_these_routes(filter_routes)
