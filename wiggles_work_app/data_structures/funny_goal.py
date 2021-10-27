from data_structures.json_mappable import *

class FunnyGoal(JsonMappable):
    def __init__(self, text = ''):
        self.text = text