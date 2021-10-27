from data_structures.json_mappable import *

class BingoGame(JsonMappable):
    def __init__(self):
        self.goals = [] # type: array of abstract goal objects

