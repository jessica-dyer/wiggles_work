from data_structures.data_structures import *
from data_structures.route_list import *
from data_structures.json_mappable import *
from data_structures.data_structures import *
from data_structures.climber import *

class DataRepository(JsonMappable):

    def __init__(self):
        self.climbers = []
        self.routes = []
        self.import_from_file()

    def add_route(self, new_route):
        self.routes.append(new_route)
        self.export_to_file()

    def update_route(self, modified_route):
        existing_index = self.routes.index(modified_route)
        self.routes[existing_index] = modified_route
        self.export_to_file()

    def delete_route(self, route):
        self.routes.remove(route)
        self.export_to_file()

    def get_route(self, route_id):
        id_as_uuid = uuid.UUID(route_id)
        matches = [r for r in self.routes if r.id == id_as_uuid]
        if len(matches) == 0:
            return None
        return matches[0]

    def add_climber(self, climber):
        self.climbers.append(climber)

    def to_dict_or_list(self):
        dictionary = {}
        dictionary["routes"] = JsonMappable.serialize_list(self.routes)
        dictionary["climbers"] = JsonMappable.serialize_list(self.climbers)
        return dictionary

    def export_to_file(self, filename='saved_routes.json'):
        dictionary = self.to_dict_or_list()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=4)

    def import_from_file(self, filename='saved_routes.json'):
        with open(filename, 'r', encoding='utf-8') as f:
            dictionary = json.load(f)
            if "routes" in dictionary.keys():
                route_dictionaries = dictionary["routes"]
                self.routes = JsonMappable.rehydrate_list(route_dictionaries, Route)
            if "climbers" in dictionary.keys():
                climber_dictionaries = dictionary["climbers"]
                self.climbers = JsonMappable.rehydrate_list(climber_dictionaries, Climber)

