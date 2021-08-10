from data_structures.data_structures import *
from wiggles_work_app import WigglesWorkApp
from data_structures.climber import *

def create_hard_coded_data(app):
    lw = Climber()
    lw.name = "Little Wiggles"
    app.data_repository.add_climber(lw)

def test():
    app = WigglesWorkApp()
    if len(app.data_repository.climbers) == 0:
        create_hard_coded_data(app)


    app.start()

test()

