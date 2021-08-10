# from data_structures.data_structures import *
# from data_structures.json_mappable import *
#
# class RouteList(JsonMappable):
#     def __init__(self):
#         self.routes = []
#
#     def to_dict(self):
#         route_dictionaries = []
#         for r in self.routes:
#             route_dictionaries.append(r.to_dict())
#         dictionary = {}
#         dictionary["routes"] = route_dictionaries
#         return dictionary
#
#     def add_route(self, new_route):
#         self.routes.append(new_route)
#
#     def update_route(self, modified_route):
#         existing_index = self.routes.index(modified_route)
#         self.routes[existing_index] = modified_route
#
#     def delete_route(self, route):
#         self.routes.remove(route)
#
#     def pretty_print_all(self):
#         for r in self.routes:
#             r.pretty_print()