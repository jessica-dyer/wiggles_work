import uuid

from data_structures.json_mappable import *

class ClimbingGoal(JsonMappable):
    def __init__(self, route_id_string = None):
        self.route_id = None #type: uuid
        if route_id_string is not None:
            self.route_id = uuid.UUID(route_id_string)