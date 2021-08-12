from data_structures.data_structures import *
from wiggles_work_app import WigglesWorkApp
from data_structures.climber import *
from data_structures import ascent

def create_hard_coded_data(app):
    lw = Climber()
    lw.name = "Little Wiggles"
    app.data_repository.add_climber(lw)

def test():
    app = WigglesWorkApp()
    ascent.wiggles_work_app = app
    if len(app.data_repository.climbers) == 0:
        create_hard_coded_data(app)

    app.start()

test()

