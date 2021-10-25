import kivy
kivy.require("1.9.1")
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.base import Builder

from ui.edit_route_screen import *
from ui.ascent_list_row_view import *
from wiggles_work_app import *
from ui.route_list_row_view import RouteListRowView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

AscentListRecycleView_in_Kivy_language = '''

AscentListRecycleView:
    data: []
    viewclass: 'AscentListRowView'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        padding: dp(10)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True

'''
class AscentListRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(AscentListRecycleView, self).__init__(**kwargs)
        self.wiggles_work_app = None
        self.current_climber = None

    def setWigglesWorkApp(self, wiggles_work_app, climber):
        self.current_climber = climber
        self.wiggles_work_app = wiggles_work_app
        self.refreshData()

    def refreshData(self):
        all_ascents = self.current_climber.get_ascents_of_route()
        # if you want to sort routes for the list view, sort them in here
        self.data = [{'ascent': r} for r in all_ascents]


class AscentListView(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=1, **kwargs)
        self.current_climber = None
        self.wiggles_work_app = None
        self.recycleView = Builder.load_string(AscentListRecycleView_in_Kivy_language)
        self.add_widget(self.recycleView)

    def set_climber(self, app, climber):
        self.wiggles_work_app = app
        self.current_climber = climber
        self.recycleView.setWigglesWorkApp(self.wiggles_work_app, self.current_climber)
