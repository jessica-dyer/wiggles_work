import json
from abc import ABC, abstractmethod
import uuid


class JsonMappable(ABC):
    @abstractmethod
    def to_dict(self):
        pass


class Route(JsonMappable):
    def __init__(self, id=uuid.uuid4()):
        self.id = id
        self.name = ""
        self.grade = ""
        self.crag = ""

    def __eq__(self, other):
        return self.id == other.id

    def to_dict(self):
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
            id = UUID(dictionary["id"])
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

    def update_route(self, modified_route):
        existing_index = self.routes.index(modified_route)
        self.routes[existing_index] = modified_route

    def pretty_print_all(self):
        for r in self.routes:
            r.pretty_print()

    def export_to_file(self, filename='saved_routes.json'):
        dictionary = self.to_dict()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=4)

    def import_from_file(self, filename='saved_routes.json'):
        with open(filename, 'r', encoding='utf-8') as f:
            dictionary = json.load(f)
            route_dictionaries = dictionary["routes"]
            for d in route_dictionaries:
                route = Route.construct_from_dict(d)
                self.routes.append(route)
