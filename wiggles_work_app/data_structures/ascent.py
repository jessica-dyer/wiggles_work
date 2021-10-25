from data_structures.json_mappable import *
from enum import Enum
import json
import uuid
from datetime import datetime

wiggles_work_app = None


class AscentType(Enum):
    TOP_ROPE = 1
    ONSIGHT = 2
    REDPOINT = 3

    def name_for_dropdown(self):
        names = {
            AscentType.TOP_ROPE.value: "Top rope",
            AscentType.ONSIGHT.value: "On sight",
            AscentType.REDPOINT.value: "Redpoint"
        }
        return names[self.value]


class Ascent(JsonMappable):
    day_format = "%Y-%m-%d"  ## format for saving to JSON
    user_facing_day_format = "%B %d, %Y"

    def __init__(self, id=uuid.uuid4()):
        self._cached_route = None
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
        if self.ascent_type is not None:
            dictionary["ascent_type"] = self.ascent_type.name
        dictionary["date"] = self.date.strftime(Ascent.day_format)
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

        try:
            ascent_type_as_string = dictionary["ascent_type"]
            ascent.ascent_type = AscentType[ascent_type_as_string]
        except:
            # print("Couldn't make an ascent type" + (ascent_type_as_string or "None"))
            pass
        day_string = dictionary["date"]
        ascent.date = datetime.strptime(day_string, Ascent.day_format)
        ascent.notes = dictionary["notes"]
        ascent.route_id = uuid.UUID(dictionary["route_id"])
        return ascent
