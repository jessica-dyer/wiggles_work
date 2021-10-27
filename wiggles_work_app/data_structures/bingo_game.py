from data_structures.json_mappable import *

class BingoGame(JsonMappable):
    def __init__(self):
        self.goals = [] # type: array of abstract goal objects

    def to_dict_or_list(self):
        dictionary = {}
        dictionary['goals'] = JsonMappable.serialize_list(self.goals, includeClassName=True)
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        bg = BingoGame()
        goal_dictionaries = dictionary['goals']
        climber.ascents = JsonMappable.rehydrate_list(goal_dictionaries)
