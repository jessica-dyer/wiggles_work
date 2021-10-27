from data_structures.route import *
from data_structures.json_mappable import *
from data_structures.route import *
from data_structures.climber import *
import json

class DataRepository(JsonMappable):

    def __init__(self):
        self.climbers = [] # type: Climber
        self.routes = [] # type: array of Route objects
        self.current_climber = None
        self.bingo_games = []
        self.import_from_file()
        self.current_climber = self.climbers[0]

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

    def delete_ascent_from_current_climber(self, ascent):
        self.current_climber.delete_ascent(ascent)
        self.export_to_file()

    def get_route(self, route_id):
        # id_as_uuid = uuid.UUID(route_id)
        id_as_uuid = route_id
        matches = [r for r in self.routes if r.id == id_as_uuid]
        if len(matches) == 0:
            return None
        return matches[0]

    def add_ascent(self, new_ascent):
        self.current_climber.ascents.append(new_ascent)
        self.export_to_file()

    def update_ascent(self, ascent):
        pass

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

    def getRoutesMatching(self, search_string):
        matched_list = []
        search_string = search_string.lower()
        for r in self.routes:
            temp_name = r.name.lower()
            if search_string in temp_name or search_string in r.grade.lower():
                matched_list.append(r)
        return matched_list