import kivy
from ui.wiggles_work_screen import *
from kivymd.uix.picker import MDDatePicker
from enum import Enum
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton
from data_structures.ascent import *


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
        self.save_ascent_button = MDFillRoundFlatButton(text="Save")
        self.screen_content.add_widget(self.save_ascent_button)
        self.save_ascent_button.bind(on_press=self.on_click_save_ascent)

        temporaryButton = MDFillRoundFlatButton(text="shit")
        temporaryButton.bind(on_press=self.show_date_picker_dialog)
        self.add_widget(temporaryButton)

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
