import kivy
from ui.wiggles_work_screen import *
from kivymd.uix.picker import MDDatePicker
from enum import Enum
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton
from data_structures.ascent import *
from ui.view_route_screen import *
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField

from kivymd.uix.dropdownitem import MDDropDownItem


class AscentScreenMode(Enum):
    ADD = 1
    EDIT = 2


class EditAscentScreen(WigglesWorkScreen):
    # Parameter 'route' is only necessary for creating brand new ascents
    # Otherwise this will use the route specified by the given ascent
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
        self.route_card = MDCard(orientation='vertical',
                                 padding=8,
                                 size_hint=(1, None),
                                 height=300,
                                 pos_hint={"center_y": .5},
                                 focus_behavior=True)
        current_route = self.ascent.get_route()
        current_route_name = current_route.name

        self.route_name = MDLabel(text=f'Route name: {current_route_name}')
        self.ascent_type_label = MDLabel(text='')
        self.update_ascent_type_label()
        self.date_label = MDLabel(text='')
        self.update_date_label()
        self.save_ascent_button = MDFillRoundFlatButton(text="Save")
        # self.screen_content.add_widget(self.save_ascent_button)
        # self.save_ascent_button.bind(on_press=self.on_click_save_ascent)
        self.bottom_button_container.add_widget(self.save_ascent_button)
        self.toolbar.left_action_items = [["arrow-left-bold", lambda x: self.on_click_back()]]
        self.notes_field = MDTextField(hint_text='Notes from the ascent:',
                                       mode='fill',
                                       fill_color=(0, 0, 0, .2),
                                       multiline=True)
        self.ascent_type_container = BoxLayout(orientation='horizontal')
        self.ascent_date_container = BoxLayout(orientation='horizontal')

        self.route_card.add_widget(self.route_name)

        self.ascent_type_container.add_widget(self.ascent_type_label)
        self.ascent_date_container.add_widget(self.date_label)

        self.route_card.add_widget(self.ascent_type_container)
        self.route_card.add_widget(self.ascent_date_container)

        self.screen_content.add_widget(self.route_card)
        self.screen_content.add_widget(self.notes_field)
        # self.screen_content.add_widget(self.bottom_button_container)
        self.select_date = MDFillRoundFlatButton(text="Select date")
        self.select_date.bind(on_press=self.show_date_picker_dialog)

        self.ascent_type_button = MDFillRoundFlatButton(text="Change")
        self.ascent_type_button.bind(on_press=self.on_dropdown_opened)

        self.ascent_type_menu = MDDropdownMenu(caller=self.ascent_type_button,
                                               items=self.build_ascent_type_menu_items(),
                                               position="center",
                                               width_mult=4)
        self.ascent_type_container.add_widget(self.ascent_type_button)
        self.ascent_date_container.add_widget(self.select_date)

    def build_ascent_type_menu_items(self):
        # all_values = AscentType.__members__.values()
        foo = []
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
        self.update_ascent_type_label()
        self.ascent_type_menu.dismiss()

    def on_dropdown_opened(self, arg2):
        self.ascent_type_menu.open()

    def update_ascent_type_label(self):
        userFacingAscentType = "Not yet set."
        if self.ascent.ascent_type is None:
            pass
        else:
            userFacingAscentType = self.ascent.ascent_type.name_for_dropdown()

        self.ascent_type_label.text = f'Ascent type: {userFacingAscentType}'

    def update_date_label(self):
        userFacingDate = 'Not yet set.'
        if self.ascent.date is None:
            pass
        else:
            userFacingDate = self.ascent.date.strftime(Ascent.user_facing_day_format)

        self.date_label.text = f'Ascent date: {userFacingDate}'

    def on_date_picked(self, datePicker, dateObject, someOtherCrap):
        self.ascent.date = dateObject

        self.update_date_label()

    def show_date_picker_dialog(self, button):
        datePicker = MDDatePicker()
        datePicker.bind(on_save=self.on_date_picked)
        datePicker.open()

    def on_click_save_ascent(self, button):
        self.ascent.notes = self.notes_field.text
        if self.mode == AscentScreenMode.ADD:
            self.wiggles_work_app.data_repository.add_ascent(self.ascent)
        else:
            self.wiggles_work_app.data_repository.update_ascent(self.ascent)

    def on_click_back(self):
        # print("You're clicking the back button")
        view_route = ViewRouteScreen(self.wiggles_work_app, self.ascent.route)
        self.wiggles_work_app.window.set_view(view_route)
