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
        pass

    # setter
    def set_route(self):
        pass

    def to_dict_or_list(self):
        return {}
