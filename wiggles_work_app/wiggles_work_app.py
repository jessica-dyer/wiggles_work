from data_repository import DataRepository
from ui.route_list_screen import RouteListScreen
from ui.edit_route_screen import EditRouteScreen
from ui.wiggles_work_window import WigglesWorkWindow
from ui.intro_screen import *
from ui.view_route_screen import *
from ui.edit_ascent_screen import *


class WigglesWorkApp:

    def __init__(self):
        self.data_repository = DataRepository()
        self.window = WigglesWorkWindow()
        self.route_list_screen = RouteListScreen(self)
        self.intro_screen = IntroductionScreen(self)
        self.window.set_view(self.intro_screen)

    def start(self):
        self.window.run()

    def navigate_to_route_list(self):
        self.route_list_screen.refreshList()
        self.window.set_view(self.route_list_screen)

    def navigate_to_edit_route(self, route):
        edit_screen = EditRouteScreen(self, route)
        self.window.set_view(edit_screen)

    def navigate_to_view_route(self, route):
        view_route = ViewRouteScreen(self, route)
        self.window.set_view(view_route)

    def navigate_to_add_ascent(self):
        edit_ascent = EditAscentScreen(self, None)
        self.window.set_view(edit_ascent)
