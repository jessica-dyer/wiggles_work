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
    a1.route_id = "4fed8026-8a33-4ebc-bd38-35b5bec55344"
    lw.ascents.append(a1)
    app.data_repository.export_to_file()

def test():
    app = WigglesWorkApp()
    ascent.wiggles_work_app = app
    if len(app.data_repository.climbers) == 0:
        create_hard_coded_data(app)
    lw = app.data_repository.climbers[0]
    n = lw.ascents[0].route.name
    print(n)
    app.start()

test()

