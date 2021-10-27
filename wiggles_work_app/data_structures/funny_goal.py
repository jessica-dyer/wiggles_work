from data_structures.abstract_goal import *

class FunnyGoal(AbstractGoal):
    def __init__(self, text = ''):
        self.text = text

    def to_dict_or_list(self):
        dictionary = {}
        dictionary['text'] = self.text
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        foo = FunnyGoal()
        foo.text = dictionary['text']
        return foo