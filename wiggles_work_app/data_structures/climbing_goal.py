import uuid

from data_structures.abstract_goal import *

class ClimbingGoal(AbstractGoal):
    def __init__(self, route_id_string = None):
        self.route_id = None #type: uuid
        if route_id_string is not None:
            self.route_id = uuid.UUID(route_id_string)

    def get_text(self):
        return 'Not yet set up'

    def is_complete(self):
        return False

    def to_dict_or_list(self):
        dictionary = {}
        dictionary['route_id'] = str(self.route_id)
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        foo = ClimbingGoal()
        foo.route_id = uuid.UUID(dictionary['route_id'])
        return foo