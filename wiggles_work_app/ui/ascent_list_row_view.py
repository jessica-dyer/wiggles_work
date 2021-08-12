import kivy
kivy.require("1.9.1")
from kivy.uix.button import Button
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
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.graphics import Color, Rectangle



class AscentListRowView(RecycleDataViewBehavior, GridLayout):
    wiggles_work_app = None
    index = None
    selected = False
    selectable = BooleanProperty(True)

    def __init__(self):
        super().__init__(cols=1)
        self.row_layout = GridLayout(rows=1)
        self.add_widget(self.row_layout, index=0)
        self.backgroundView = Widget()
        self.add_widget(self.backgroundView, 1)
        self.ascent = None
        self.name_label = Label(text="jklfdsfasd;jkl")
        self.row_layout.add_widget(self.name_label)
        

    def refresh_view_attrs(self, rv, index, data_item):
        self.wiggles_work_app = rv.wiggles_work_app
        self.index = index
        self.ascent = data_item["ascent"]
        # self.name_label.text = self.route.name
        # self.grade_label.text = self.route.grade
        self.size = self.row_layout.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.selectable:
            self.selected = True
            with self.backgroundView.canvas:
                Color(1, 1, 1, 0.75)  # color for highlight on click
                Rectangle(pos=self.pos, size=self.size)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos) and self.selected:
            self.onRowClicked()
        self.backgroundView.canvas.clear()
        self.selected = False

    def onRowClicked(self):
        print("Little Wiggles is funny and cute!")
        # self.wiggles_work_app.navigate_to_edit_route(self.route)