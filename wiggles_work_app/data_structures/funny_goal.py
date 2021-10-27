from data_structures.abstract_goal import *

class FunnyGoal(AbstractGoal):
    def __init__(self, text = ''):
        self.text = text

    def get_text(self):
        return self.text

    def is_complete(self):
        return False

    def to_dict_or_list(self):
        dictionary = {}
        dictionary['text'] = self.text
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        foo = FunnyGoal()
        if 'text' in dictionary.keys():
            foo.text = dictionary['text']
        return foo