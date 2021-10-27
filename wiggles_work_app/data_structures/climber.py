from data_structures.route import *
from data_structures.ascent import *
from data_structures.json_mappable import *


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

    def delete_ascent(self, ascent):
        self.ascents.remove(ascent)

    def get_ascents_of_route(self, current_route):
        # return array of ascents that match the route id in route object
        filtered_ascents = []
        for item in self.ascents:
            if item.route_id == current_route.id:
                filtered_ascents.append(item)
        filtered_ascents.sort(key=lambda x: x.date, reverse=True)
        return filtered_ascents
