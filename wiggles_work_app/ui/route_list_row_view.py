from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from ui.color import WWColors
from kivymd.uix.label import MDLabel


class RouteListRowView(RecycleDataViewBehavior, GridLayout):
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
        self.route = None
        self.name_label = MDLabel(text="")
        self.grade_label = MDLabel(text="", halign='center')
        self.row_layout.add_widget(self.grade_label)
        self.row_layout.add_widget(self.name_label)

    def refresh_view_attrs(self, rv, index, data_item):
        self.wiggles_work_app = rv.wiggles_work_app
        self.index = index
        self.route = data_item["route"]
        self.name_label.text = self.route.name
        self.grade_label.text = self.route.grade
        self.size = self.row_layout.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.selectable:
            self.selected = True
            with self.backgroundView.canvas:
                # Color(0,1,0,1)
                # WWColors.ROW_CLICK_HIGHLIGHT_STUPID  # color for highlight on click
                self.backgroundView.canvas.add(WWColors.ROW_CLICK_HIGHLIGHT)
                Rectangle(pos=self.pos, size=self.size)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos) and self.selected:
            self.onRowClicked()
        self.backgroundView.canvas.clear()
        self.selected = False

    def onRowClicked(self):
        print("Navigating to route " + self.route.name)
        self.wiggles_work_app.navigate_to_edit_route(self.route)
