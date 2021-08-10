from data_structures.data_structures import *
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

    def delete_route(self, route):
        self.routes.remove(route)

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