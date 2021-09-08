import kivy
from ui.wiggles_work_screen import *
from kivymd.uix.picker import MDDatePicker
from enum import Enum
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton
from data_structures.ascent import *
from ui.view_route_screen import *
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem


class AscentScreenMode(Enum):
    ADD = 1
    EDIT = 2


class EditAscentScreen(WigglesWorkScreen):

    def __init__(self, wiggles_work_app, ascent=None, route=None):
        super().__init__()
        if ascent is not None and route is not None:
            raise Exception("Only pass in a route if adding a brand new ascent.")

        if ascent is None:
            self.ascent = Ascent()
            self.ascent.route_id = route.id
            self.mode = AscentScreenMode.ADD
        else:
            self.ascent = ascent
            self.mode = AscentScreenMode.EDIT

        self.wiggles_work_app = wiggles_work_app
        self.screen_header = MDLabel(text="ADD & EDIT ASCENT",
                                     halign='center',
                                     font_style='H4')
        self.save_ascent_button = MDFillRoundFlatButton(text="Save")
        self.screen_content.add_widget(self.screen_header)
        self.screen_content.add_widget(self.save_ascent_button)
        self.save_ascent_button.bind(on_press=self.on_click_save_ascent)
        self.toolbar.left_action_items = [["arrow-left-bold", lambda x: self.on_click_back()]]

        self.select_date = MDFillRoundFlatButton(text="Select date")
        self.select_date.bind(on_press=self.show_date_picker_dialog)
        self.add_widget(self.select_date)

        self.ascent_type_button = MDFillRoundFlatButton(text="Foo")
        self.ascent_type_button.bind(on_press=self.on_dropdown_opened)
        self.screen_content.add_widget(self.ascent_type_button)

        self.ascent_type_menu = MDDropdownMenu(caller=self.ascent_type_button,
                                               items=self.build_ascent_type_menu_items(),
                                               position="center",
                                               width_mult=4)

    def build_ascent_type_menu_items(self):
        # all_values = AscentType.__members__.values()
        foo =[]
        for type in AscentType:
            dict = {
                "text": type.name_for_dropdown(),
                "viewclass": "OneLineListItem",
                "on_release": lambda x=type: self.on_dropdown_item_selected(x)}
            foo.append(dict)
        return foo

    def on_dropdown_item_selected(self, selected_type):
        # self.ascent_type_button.(self.ascent_type_menu.text)
        self.ascent.ascent_type = selected_type
        self.ascent_type_menu.dismiss()

    def on_dropdown_opened(self, arg2):
        self.ascent_type_menu.open()

    def on_date_picked(self, datePicker, dateObject, someOtherCrap):
        self.ascent.date = dateObject

    def show_date_picker_dialog(self, button):
        datePicker = MDDatePicker()
        datePicker.bind(on_save=self.on_date_picked)
        datePicker.open()

    def on_click_save_ascent(self, button):
        if self.mode == AscentScreenMode.ADD:
            self.wiggles_work_app.data_repository.add_ascent(self.ascent)
        else:
            self.wiggles_work_app.data_repository.update_ascent(self.ascent)

    def on_click_back(self):
        # print("You're clicking the back button")
        view_route = ViewRouteScreen(self.wiggles_work_app, self.ascent.route)
        self.wiggles_work_app.window.set_view(view_route)
