from data_repository import DataRepository
from ui.route_list_screen import RouteListScreen
from ui.wiggles_work_window import WigglesWorkWindow

class WigglesWorkApp:

    def __init__(self):
        self.data_repository = DataRepository()
        self.route_list_screen = RouteListScreen(self)
        self.window = WigglesWorkWindow(self.route_list_screen)

    def start(self):
        self.window.run()

    def navigate_to_route_list(self):
        self.window.set_view(self.route_list_screen)