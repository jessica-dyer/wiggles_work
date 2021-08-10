from data_structures.data_structures import *

class Climber(JsonMappable):

    def __init__(self, id=uuid.uuid4()):
        self.id = id
        self.name = ""
        self.ascents = []

    def add_ascent(self, ascent):
        self.ascents.append(ascent)