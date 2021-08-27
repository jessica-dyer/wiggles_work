import kivy
from ui.wiggles_work_screen import *
from kivymd.uix.picker import MDDatePicker
from enum import Enum
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton



class AscentScreenMode(Enum):
    ADD = 1
    EDIT = 2


class EditAscentScreen(WigglesWorkScreen):

    def __init__(self, wiggles_work_app, ascent):
        super().__init__()

        if ascent is None:
            self.mode = AscentScreenMode.ADD
        else:
            self.mode = AscentScreenMode.EDIT

        self.ascent = ascent
        self.wiggles_work_app = wiggles_work_app
        # self.date_picker = MDDatePicker()
        # self.date_dialog = MDDatePicker(on_save=self.on_date_picked)

        # self.date_picker.bind(date=self.on_date_picked)
        #self.screen_content.add_widget(self.date_picker)

        temporaryButton = MDFillRoundFlatButton(text="shit"
                                            )
        temporaryButton.bind(on_press=self.show_date_picker_dialog)
        self.add_widget(temporaryButton)

    def on_date_picked(self, datePicker, dateObject, someOtherCrap):
        self.ascent.date = dateObject

    def show_date_picker_dialog(self, button):
        datePicker = MDDatePicker()
        datePicker.bind(on_save=self.on_date_picked)
        datePicker.open()

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog.open()