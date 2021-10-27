from data_structures.abstract_goal import *

class FunnyGoal(AbstractGoal):
    def __init__(self, text = ''):
        self.text = text

    def to_dict_or_list(self):
        dictionary = {}
        # dictionary['goals'] = JsonMappable.serialize_list(self.goals)
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        foo = FunnyGoal()
        # goal_dictionaries = dictionary['goals']
        # climber.ascents = JsonMappable.rehydrate_list()
        return foo