class Route:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def pretty_print(self):
        """Nicely prints the route name and grade."""
        print(f"The route name is {self.name} and the grade is {self.grade}")


class RouteList:
    def __init__(self):
        self.routes = []

    def add_route(self, new_route):
        self.routes.append(new_route)

    def pretty_print_all(self):
        for r in self.routes:
            r.pretty_print()

    def export_to_file(self, filename):
        # This will export all routes to JSON file

    def import_from_file(self, filename):
        # to do--We want the routes to import from JSON file

def test():
    x = Route("Outer Space", "5.9+")
    master_list = RouteList()
    master_list.add_route(x)
    master_list.pretty_print_all()


test()

