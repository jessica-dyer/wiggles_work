from data_structures.route import *
from wiggles_work_app import WigglesWorkApp
from data_structures.climber import *
from data_structures import ascent
from data_structures.ascent import *
from data_structures.bingo_game import *
from data_structures.funny_goal import *
from data_structures.climbing_goal import *


def create_hard_coded_data(app):
    lw = Climber()
    lw.name = "Little Wiggles"
    app.data_repository.add_climber(lw)
    a1 = Ascent()
    a1.route_id = "9ff8d5b2-813d-4e73-8595-1ab670178a5e"
    lw.ascents.append(a1)
    app.data_repository.export_to_file()

def create_hard_coded_bingo_game(app):
    my_game = BingoGame()
    my_game.goals.append(FunnyGoal(text='Little wiggles is funny and cute!'))
    my_game.goals.append(ClimbingGoal(route_id_string='28c57fc8-c8a8-4629-898c-52f947ffdb16'))

    my_game.goals.append(FunnyGoal(text='Walked all day, did not find crag!'))
    my_game.goals.append(FunnyGoal(text='Ate gummy candy for lunch!'))
    my_game.goals.append(ClimbingGoal(route_id_string='4d5167f6-0f30-4b91-a5ee-2c8d0ffc0ae9'))
    my_game.goals.append(FunnyGoal(text='Big wiggles wiggled!'))
    my_game.goals.append(FunnyGoal(text='Hangdogged!'))
    my_game.goals.append(FunnyGoal(text='Wore crocs!'))
    my_game.goals.append(FunnyGoal(text='Cheered on a stranger!'))

    app.data_repository.bingo_games.append(my_game)
    app.data_repository.export_to_file()


def run_the_thing():
    app = WigglesWorkApp()
    ascent.wiggles_work_app = app
    if len(app.data_repository.climbers) == 0:
        create_hard_coded_data(app)
    if len(app.data_repository.bingo_games) == 0:
        create_hard_coded_bingo_game(app)
    app.start()


run_the_thing()

import kivy
import kivymd

print("Using Kivy version " + kivy.__version__)
print("Using KivyMD verson " + kivymd.__version__)