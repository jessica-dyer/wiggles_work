from data_structures.json_mappable import *


class AbstractGoal(JsonMappable):
    def __init__(self):
        pass

    def get_text(self):
        return 'Nothing'
