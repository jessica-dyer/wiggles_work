from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.graphics import Color, Rectangle

class RouteListRowView(RecycleDataViewBehavior, GridLayout):
    wiggles_work_app = None
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def __init__(self):
        super().__init__(cols=5)
        self.route = None
        #self.label = Label(text=route.name)
        self.label = Label(text="Foo")
        self.add_widget(self.label)

    def refresh_view_attrs(self, rv, index, data_item):
        self.wiggles_work_app = rv.wiggles_work_app
        self.index = index
        self.route = data_item["route"]
        self.label.text = self.route.name

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.selectable:
            with self.canvas:
                Color(1,1,1,0.75)   # color for highlight on click
                Rectangle(pos=self.pos, size=self.size)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos) and self.selectable:
            self.onRowClicked()
            # with self.canvas:
            #     Color(0,0,0,1)      # color to revert too after highlight goes away
            #     Rectangle(pos=self.pos, size=self.size)

        return super(GridLayout, self).on_touch_up(touch)

    def onRowClicked(self):
        self.wiggles_work_app.navigate_to_edit_route(self.route)
