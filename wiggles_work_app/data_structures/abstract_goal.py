from data_structures.json_mappable import *


class AbstractGoal(JsonMappable):
    def __init__(self):
        pass

    def get_text(self):
        return 'Nothing'

    def to_dict_or_list(self):
         pass

    @classmethod
    def construct_from_dict(cls, dictionary):
        pass
