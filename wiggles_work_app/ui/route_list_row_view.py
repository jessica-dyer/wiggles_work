from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior

class RouteListRowView(RecycleDataViewBehavior, GridLayout):
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