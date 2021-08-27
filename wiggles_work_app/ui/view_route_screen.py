import kivy
from ui.wiggles_work_screen import *
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton
from wiggles_work_app import *
from kivymd.uix.card import MDCard
from kivy.base import Builder

card_helper = KV = '''
MDCard:
    orientation: "vertical"
    padding: "8dp"
    size_hint: None, None
    size: "280dp", "180dp"
    pos_hint: {"center_x": .5, "center_y": .5}

    MDLabel:
        text: "Title"
        theme_text_color: "Secondary"
        adaptive_height: True

    MDSeparator:
        height: "1dp"

    MDLabel:
        text: "Body"
'''

class ViewRouteScreen(WigglesWorkScreen):
    def __init__(self, wiggles_work_app, route):
        super().__init__()
        self.wiggles_work_app = wiggles_work_app
        self.route = route
        self.name_field = MDLabel(text="Route name: " + self.route.name)
        # self.screen_content.add_widget(self.name_field)
        self.edit_route_button = MDFillRoundFlatButton(text="Edit Route Details")
        self.bottom_button_container.add_widget(self.edit_route_button)
        # self.route_card = MDCard(orientation='vertical',
        #                          padding=8,
        #                          size_hint=(None, None),
        #                          size=(280, 180),
        #                          pos_hint={"center_x": .5, "center_y": .5},
        #                          focus_behavior=True)
        # self.route_card.add_widget(self.name_field)
        self.route_card = Builder.load_string(card_helper)
        self.screen_content.add_widget(self.route_card)
        self.edit_route_button.bind(on_press=self.onEditRouteButtonClicked)

    def onEditRouteButtonClicked(self, button):
        self.wiggles_work_app.navigate_to_edit_route(self.route)