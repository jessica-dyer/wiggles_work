import kivy

kivy.require("1.9.1")
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from ui.form_field import *
from enum import Enum
from data_structures.data_structures import *
from ui.delete_confirmation_screen import *
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from ui.ascent_list_view import *
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivymd.uix.dialog import MDDialog
from background_color_debugging import *
from kivymd.uix.textfield import MDTextField


class RouteScreenMode(Enum):
    ADD = 1
    EDIT = 2


class EditRouteScreen(BoxLayout):

    def __init__(self, wiggles_work_app, route):
        super().__init__(orientation='vertical',
                         padding=10,
                         spacing=7)

        if route is None:
            self.mode = RouteScreenMode.ADD
        else:
            self.mode = RouteScreenMode.EDIT
        self.route = route  # If route is 'None' it is an add not an edit
        self.wiggles_work_app = wiggles_work_app
        # self.form_field_grid_layout = GridLayout(cols=1,
        #                                          size_hint=(1, 30))
        # NEED TO UPDATE THESE FORM FIELDS TO KIVYMD
        # self.name_field = FormField("Route Name:", "")
        # self.grade_field = FormField("Grade:", "")
        # self.crag_field = FormField("Crag:", "")
        self.name_field = MDTextField(hint_text="Route Name:",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.8})
        self.grade_field = MDTextField(hint_text="Grade:",
                                       pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.crag_field = MDTextField(hint_text="Crag:",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.6})
        
        # self.add_widget(self.form_field_grid_layout)
        # self.form_field_grid_layout.add_widget(self.name_field)
        # self.form_field_grid_layout.add_widget(self.grade_field)
        # self.form_field_grid_layout.add_widget(self.crag_field)

        self.add_widget(self.name_field)
        self.add_widget(self.grade_field)
        self.add_widget(self.crag_field)

        self.current_climber = self.wiggles_work_app.data_repository.climbers[0]
        self.ascent_list_view = AscentListView(size_hint=(1, 60))
        self.ascent_list_view.set_climber(self.wiggles_work_app, self.current_climber)
        self.add_widget(self.ascent_list_view)

        # BUTTON CONTAINERS TO HOLD THE BUTTONS ON THE BOTTOM OF THE SCREEN
        # self.cancel_button = MDRectangleFlatButton(text="Cancel",
        #                                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # self.delete_button = MDRectangleFlatButton(text="Delete route",
        #                                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                                            on_release=self.show_delete_warning)
        # self.save_button = MDRectangleFlatButton(text="Save",
        #                                          pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.cancel_button = MDRectangleFlatButton(text="Cancel")
        self.delete_button = MDRectangleFlatButton(text="Delete route",
                                                   on_release=self.show_delete_warning)
        self.save_button = MDRectangleFlatButton(text="Save")
        self.save_button.bind(on_press=self.on_click_save)
        self.cancel_button.bind(on_press=self.on_click_cancel)

        self.button_inner_container = GridLayout(rows=1,
                                                 padding=8,
                                                 spacing=15,
                                                 pos_hint={'center_x': 0.5},
                                                 size_hint=(None, None),
                                                 size=(0, 80))

        self.button_inner_container.add_widget(self.cancel_button)
        if self.mode == RouteScreenMode.EDIT:
            self.button_inner_container.add_widget(self.delete_button)
        self.button_inner_container.add_widget(self.save_button)
        self.button_inner_container.do_layout()
        self.button_inner_container.width = self.button_inner_container.minimum_width

        self.add_widget(self.button_inner_container)

        if self.route is not None:
            self.name_field.text = self.route.name
            self.grade_field.text = self.route.grade
            self.crag_field.text = self.route.crag

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

    # def on_click_delete(self, button):
    #     foo = DeleteConfirmationScreen(self.wiggles_work_app, self.route.name, self, self.on_delete_confirmed)
    #     self.wiggles_work_app.window.set_view(foo)

    def show_delete_warning(self, obj):
        cancel_button = MDRectangleFlatButton(text='Cancel', on_release=self.close_dialog)
        delete_button = MDRectangleFlatButton(text='I really want to delete!', on_release=self.on_delete_confirmed)
        self.dialog_box = MDDialog(title='Delete confirmation',
                                   buttons=[cancel_button, delete_button])
        self.dialog_box.open()

    def close_dialog(self, obj):
        self.dialog_box.dismiss

    def on_delete_confirmed(self, obj):
        self.wiggles_work_app.data_repository.delete_route(self.route)
        self.wiggles_work_app.navigate_to_route_list()
        self.dialog_box.dismiss
