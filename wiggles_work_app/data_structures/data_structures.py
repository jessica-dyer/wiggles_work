import json
import uuid
from data_structures.json_mappable import *


class Route(JsonMappable):
    def __init__(self, id=uuid.uuid4()):
        self.id = id
        self.name = ""
        self.grade = ""
        self.crag = ""

    def __eq__(self, other):
        return self.id == other.id

    def to_dict_or_list(self):
        dictionary = {}
        dictionary["id"] = str(self.id)
        dictionary["name"] = self.name
        dictionary["grade"] = self.grade
        dictionary["crag"] = self.crag
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        id = None
        if "id" in dictionary.keys():
            id = uuid.UUID(dictionary["id"])
        else:
            id = uuid.uuid4()
        route = Route(id)
        route.name = dictionary["name"]
        route.grade = dictionary["grade"]
        route.crag = dictionary["crag"]
        return route



    def pretty_print(self):
        """Nicely prints the route name and grade."""
        print(
            f"The route name is {self.name} and the grade is {self.grade}. This route is located at the {self.crag} crag.")

