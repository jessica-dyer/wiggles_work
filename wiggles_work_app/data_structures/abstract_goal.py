from data_structures.json_mappable import *
from abc import ABC, abstractmethod

class AbstractGoal(JsonMappable):
    def __init__(self):
        pass

    @abstractmethod
    def get_text(self):
        return 'Nothing'

    @abstractmethod
    def is_complete(self):
        return False

    @abstractmethod
    def to_dict_or_list(self):
         pass

    @classmethod
    def construct_from_dict(cls, dictionary):
        pass
