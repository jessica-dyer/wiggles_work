from data_structures.json_mappable import *
from enum import Enum

class AscentType(Enum):
    TOP_ROPE = 1
    ONSIGHT = 2

class Ascent(JsonMappable):
    def __init__(self, id=uuid.uuid4()):
        self.id = id
        self.ascent_type = None
        self.date = None
        self.notes = ""
        self.route = None
