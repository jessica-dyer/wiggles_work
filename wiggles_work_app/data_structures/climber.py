from data_structures.data_structures import *
from data_structures.ascent import *

class Climber(JsonMappable):

    def __init__(self, id=uuid.uuid4()):
        self.id = id
        self.name = ""
        self.ascents = []

    def to_dict_or_list(self):
        dictionary = {}
        dictionary["id"] = str(self.id)
        dictionary["name"] = self.name
        dictionary["ascents"] = JsonMappable.serialize_list(self.ascents)
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        id = None
        if "id" in dictionary.keys():
            id = uuid.UUID(dictionary["id"])
        else:
            id = uuid.uuid4()
        climber = Climber(id)
        climber.name = dictionary["name"]
        ascent_dictionaries = dictionary["ascents"]
        climber.ascents = JsonMappable.rehydrate_list(ascent_dictionaries, Ascent)
        return climber

    def add_ascent(self, ascent):
        self.ascents.append(ascent)
