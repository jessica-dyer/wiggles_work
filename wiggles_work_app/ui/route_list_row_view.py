from ui.wiggles_row_view import WigglesRowView

from kivymd.uix.label import MDLabel

from background_color_debugging import *


class RouteListRowView(WigglesRowView):
    wiggles_work_app = None

    def __init__(self):
        super().__init__()
        self.route = None
        self.name_label = MDLabel(text="")
        self.grade_label = MDLabel(text="", halign='center')
        self.grade_label.size_hint_x = None
        self.grade_label.width = 80
        self.row_layout.add_widget(self.grade_label)
        self.row_layout.add_widget(self.name_label)

    def refresh_view_attrs(self, rv, index, data_item):
        self.wiggles_work_app = rv.wiggles_work_app
        self.index = index
        self.route = data_item["route"]
        self.name_label.text = self.route.name
        self.grade_label.text = self.route.grade

    def onRowClicked(self):
        self.wiggles_work_app.navigate_to_view_route(self.route)
