from abc import ABC, abstractmethod
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from ui.color import WWColors
from kivymd.uix.list import *

class WigglesRowView(RecycleDataViewBehavior, BaseListItem):
    index = None
    selected = False
    selectable = BooleanProperty(True)

    def __init__(self):
        super().__init__()
        self.row_layout = BoxLayout(orientation="horizontal")
        self.add_widget(self.row_layout, index=0)
        self.backgroundView = Widget()
        self.add_widget(self.backgroundView, 1)

    def on_pos(self, widget, pos):
        self.row_layout.size_hint = (1, None)
        self.row_layout.height = self.height
        self.row_layout.pos = self.pos

    def on_touch_down(self, touch):
        # super().on_touch_down(touch)
        if self.collide_point(*touch.pos) and self.selectable:
            self.selected = True
            with self.backgroundView.canvas:
                self.backgroundView.canvas.add(WWColors.ROW_CLICK_HIGHLIGHT)
                Rectangle(pos=self.pos, size=self.size)

    def on_touch_up(self, touch):
        # super().on_touch_up(touch)
        if self.collide_point(*touch.pos) and self.selected:
            self.onRowClicked()
        self.backgroundView.canvas.clear()
        self.selected = False

    @abstractmethod
    def onRowClicked(self):
        pass