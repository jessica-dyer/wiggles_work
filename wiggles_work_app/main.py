from data_structures.data_structures import *
from wiggles_work_app import WigglesWorkApp
from data_structures.climber import *
from data_structures import ascent
from data_structures.ascent import *


def create_hard_coded_data(app):
    lw = Climber()
    lw.name = "Little Wiggles"
    app.data_repository.add_climber(lw)
    a1 = Ascent()
    a1.route_id = "9ff8d5b2-813d-4e73-8595-1ab670178a5e"
    lw.ascents.append(a1)
    app.data_repository.export_to_file()


def test():
    app = WigglesWorkApp()
    ascent.wiggles_work_app = app
    if len(app.data_repository.climbers) == 0:
        create_hard_coded_data(app)

    app.start()


test()
