import kivy

kivy.require("1.9.1")
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.base import Builder

from ui.edit_route_screen import *
from wiggles_work_app import *
from ui.wiggles_row_view import WigglesRowView
from data_structures.ascent import *
from kivymd.uix.label import MDLabel



class AscentListRowView(WigglesRowView):
    wiggles_work_app = None

    def __init__(self):
        super().__init__()
        self.ascent = None
        self.name_label = MDLabel(text="")
        self.row_layout.add_widget(self.name_label)
        

    def refresh_view_attrs(self, rv, index, data_item):
        self.wiggles_work_app = rv.wiggles_work_app
        self.index = index
        self.ascent = data_item["ascent"]
        self.name_label.text = self.ascent.date.strftime(Ascent.user_facing_day_format)
        # self.name_label.text = self.ascent.id
        # self.grade_label.text = self.route.grade
        self.size = self.row_layout.size

    def onRowClicked(self):
        self.wiggles_work_app.navigate_to_edit_ascent(self.ascent)