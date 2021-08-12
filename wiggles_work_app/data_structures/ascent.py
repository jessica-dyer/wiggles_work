from data_structures.json_mappable import *
from enum import Enum
import json
import uuid

wiggles_work_app = None

class AscentType(Enum):
    TOP_ROPE = 1
    ONSIGHT = 2

class Ascent(JsonMappable):
    def __init__(self, id=uuid.uuid4()):
        self.id = id
        self.ascent_type = None
        self.date = None
        self.notes = ""
        self.route_id = None

    # getter
    def get_route(self):
        if self._cached_route is None:
            self._cached_route = wiggles_work_app.data_repository.get_route(self.route_id)

        return self._cached_route

    # setter
    def set_route(self, route_object):
        self._cached_route = route_object
        self.route_id = route_object.id

    # creating a property object
    route = property(get_route, set_route)

    def to_dict_or_list(self):
        dictionary = {}
        dictionary["id"] = str(self.id)
        dictionary["ascent_type"] = self.ascent_type
        dictionary["dates"] = self.dates
        dictionary["notes"] = self.notes
        dictionary["route_id"] = str(self.route_id)
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        id = None
        if "id" in dictionary.keys():
            id = uuid.UUID(dictionary["id"])
        else:
            id = uuid.uuid4()
        ascent = Ascent(id)
        ascent.ascent_type = dictionary["ascent_type"]
        ascent.dates = dictionary["dates"]
        ascent.notes = dictionary["notes"]
        ascent.route_id = uuid.UUID(dictionary["route_id"])
        return ascent
