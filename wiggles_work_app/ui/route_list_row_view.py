from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty

class RouteListRowView(RecycleDataViewBehavior, GridLayout):
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
        self.route = data_item["route"]
        self.label.text = self.route.name

    def on_touch_down(self, touch):
        print("how about this?")

    def apply_selection(self, rv, index, is_selected):
        print("what does this do?")
        if is_selected:
            print("I'm selected!  " + self.route.name)

    def on_touch_up(self, touch):
        print("touch up in  " + self.route.name)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(GridLayout, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            print("here for  " + self.route.name)
            return self.parent.select_with_touch(self.index, touch)