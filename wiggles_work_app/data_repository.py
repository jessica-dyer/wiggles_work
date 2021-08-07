from data_structures.data_structures import *

class DataRepository:

    def __init__(self):
        self.master_list = RouteList()
        self.master_list.import_from_file()

    def add_route(self, new_route):
        self.master_list.add_route(new_route)
        self.master_list.export_to_file()

    def update_route(self, modified_route):
        self.master_list.update_route(modified_route)
        self.master_list.export_to_file()
