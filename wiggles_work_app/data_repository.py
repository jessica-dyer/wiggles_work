from data_structures.data_structures import *

class DataRepository:

    def __init__(self):
        self.master_list = RouteList()
        self.master_list.import_from_file()