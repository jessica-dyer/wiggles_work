import kivy
from ui.wiggles_work_screen import *
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton
from wiggles_work_app import *
from kivymd.uix.card import MDCard
from kivy.base import Builder
from ui.ascent_list_view import *


helper = '''
MDSeparator: 
    height: "1dp"
'''


class ViewRouteScreen(WigglesWorkScreen):
    def __init__(self, wiggles_work_app, route):
        super().__init__()
        self.wiggles_work_app = wiggles_work_app
        self.route = route
        self.title_field = MDLabel(text="Route details",
                                   theme_text_color="Secondary",
                                   adaptive_height=True)
        self.route_name = MDLabel(text=self.route.name,
                                  pos_hint={"center_x": .5, "center_y": .5})
        self.route_grade = MDLabel(text=self.route.grade,
                                   pos_hint={"center_x": .5, "center_y": .5})
        self.route_crag = MDLabel(text=self.route.crag,
                                  pos_hint={"center_x": .5, "center_y": .5})
        # self.screen_content.add_widget(self.name_field)
        self.edit_route_button = MDFillRoundFlatButton(text="Edit Route Details")
        self.add_ascent_button = MDFillRoundFlatButton(text="I climbed this!")

        self.route_card = MDCard(orientation='vertical',
                                 padding=8,
                                 size_hint=(1, None),
                                 height=200,
                                 pos_hint={"center_x": .5, "center_y": .5},
                                 focus_behavior=True)
        self.horizontal_line = Builder.load_string(helper)
        self.route_card.add_widget(self.title_field)
        self.route_card.add_widget(self.horizontal_line)
        self.route_card.add_widget(self.route_name)
        self.route_card.add_widget(self.route_grade)
        self.route_card.add_widget(self.route_crag)
        self.route_card.add_widget(self.edit_route_button)
        self.screen_content.add_widget(self.route_card)
        self.edit_route_button.bind(on_press=self.onEditRouteButtonClicked)
        self.add_ascent_button.bind(on_press=self.iClimbedThisClicked)

        self.current_climber = self.wiggles_work_app.data_repository.climbers[0]
        self.ascent_list_view = AscentListView(size_hint=(1, 60))
        self.ascent_list_view.set_climber(self.wiggles_work_app, self.current_climber)
        self.screen_content.add_widget(self.ascent_list_view)

        self.bottom_button_container.add_widget(self.add_ascent_button)


    def onEditRouteButtonClicked(self, button):
        self.wiggles_work_app.navigate_to_edit_route(self.route)

    def iClimbedThisClicked(self, button):
        self.wiggles_work_app.navigate_to_add_ascent(self.route)
