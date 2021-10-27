import uuid

from data_structures.abstract_goal import *

class ClimbingGoal(AbstractGoal):
    def __init__(self, route_id_string = None):
        self.route_id = None #type: uuid
        if route_id_string is not None:
            self.route_id = uuid.UUID(route_id_string)

    def to_dict_or_list(self):
        dictionary = {}
        # dictionary['goals'] = JsonMappable.serialize_list(self.goals)
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        foo = ClimbingGoal()
        # goal_dictionaries = dictionary['goals']
        # climber.ascents = JsonMappable.rehydrate_list()
        return foo