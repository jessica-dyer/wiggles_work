from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget


class RouteListRowView(RecycleDataViewBehavior, GridLayout):
    wiggles_work_app = None
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def __init__(self):
        super().__init__(cols=1)
        self.grid_layout = GridLayout(cols=5)
        self.add_widget(self.grid_layout, index=0)
        self.backgroundView = Widget()
        self.add_widget(self.backgroundView, 1)
        self.route = None
        self.name_label = Label(text="")
        self.grade_label = Label(text="")
        self.grid_layout.add_widget(self.name_label)
        self.grid_layout.add_widget(self.grade_label)

    def refresh_view_attrs(self, rv, index, data_item):
        self.wiggles_work_app = rv.wiggles_work_app
        self.index = index
        self.route = data_item["route"]
        self.name_label.text = self.route.name
        self.grade_label.text = self.route.grade
        self.size = self.grid_layout.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.selectable:
            with self.backgroundView.canvas:
                Color(1,1,1,0.75)   # color for highlight on click
                Rectangle(pos=self.pos, size=self.size)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos) and self.selectable:
            self.onRowClicked()
            self.backgroundView.canvas.clear()


    def onRowClicked(self):
        print("Navigating to route " + self.route.name)
        self.wiggles_work_app.navigate_to_edit_route(self.route)
