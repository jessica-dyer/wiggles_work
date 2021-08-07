from data_structures.data_structures import *
from ui.route_list_screen import RouteListScreen


def test():
    # x = Route("Outer Space", "5.9+", "Snow Creek")
    master_list = RouteList()
    # master_list.add_route(x)
    master_list.import_from_file()
    master_list.pretty_print_all()
    master_list.export_to_file()
    route_list_window = RouteListScreen()
    route_list_window.run()


test()

