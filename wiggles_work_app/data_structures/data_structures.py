import json
from abc import ABC, abstractmethod
class JsonMappable(ABC):
    @abstractmethod
    def to_dict(self):
        pass

class Route(JsonMappable):
    def __init__(self, name, grade, crag):
        self.name = name
        self.grade = grade
        self.crag = crag

    def to_dict(self):
        dictionary = {}
        dictionary["name"] = self.name
        dictionary["grade"] = self.grade
        dictionary["crag"] = self.crag
        return dictionary

    @classmethod
    def construct_from_dict(cls, dictionary):
        return Route(dictionary["name"],
                     dictionary["grade"],
                     dictionary["crag"])

    def pretty_print(self):
        """Nicely prints the route name and grade."""
        print(f"The route name is {self.name} and the grade is {self.grade}. This route is located at the {self.crag} crag.")


class RouteList(JsonMappable):
    def __init__(self):
        self.routes = []

    def to_dict(self):
        route_dictionaries = []
        for r in self.routes:
            route_dictionaries.append(r.to_dict())
        dictionary = {}
        dictionary["routes"] = route_dictionaries
        return dictionary

    def add_route(self, new_route):
        self.routes.append(new_route)

    def pretty_print_all(self):
        for r in self.routes:
            r.pretty_print()

    def export_to_file(self, filename = 'saved_routes.json'):
        dictionary = self.to_dict()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=4)

    def import_from_file(self, filename = 'saved_routes.json'):
        with open(filename, 'r', encoding='utf-8') as f:
            dictionary = json.load(f)
            route_dictionaries = dictionary["routes"]
            for d in route_dictionaries:
                route = Route.construct_from_dict(d)
                self.routes.append(route)