import kivy
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton
from kivy.uix.image import Image
from background_color_debugging import *


class IntroductionScreen(MDScreen):
    def __init__(self, wiggles_work_app, **kwargs):
        super().__init__(**kwargs)

        self.wiggles_work_app = wiggles_work_app
        self.screen_box_layout = BoxLayout(orientation='vertical',
                                           # adaptive_height=True,
                                           spacing=60,
                                           padding=50,
                                           pos_hint={'center_x': 0.5})
        self.logo = Image(source='kg-harness-01.png',
                          size_hint=(None, None),
                          pos_hint={'center_x': 0.5})
        self.box_layout_text_fields = BoxLayout(orientation='vertical',
                                                spacing=20)
        self.box_layout_button = BoxLayout(orientation='vertical',
                                           spacing=20)
        self.username = MDTextField(hint_text="Username",
                                    mode='fill',
                                    line_anim=False,
                                    fill_color=(0, 0, 0, .2))
        self.password = MDTextField(hint_text="Password",
                                    mode='fill',
                                    password=True,
                                    password_mask="*",
                                    fill_color=(0, 0, 0, .2))
        self.enter_button = MDFillRoundFlatButton(text="Play!",
                                                  pos_hint={'center_x': 0.5},
                                                  _no_ripple_effect=True)
        self.enter_button.bind(on_press=self.on_click_enter)

        self.box_layout_text_fields.add_widget(self.username)
        self.box_layout_text_fields.add_widget(self.password)

        self.box_layout_button.add_widget(self.enter_button)

        self.screen_box_layout.add_widget(self.logo)
        self.screen_box_layout.add_widget(self.box_layout_text_fields)
        self.screen_box_layout.add_widget(self.box_layout_button)
        self.add_widget(self.screen_box_layout)

    def on_click_enter(self, button):
        self.wiggles_work_app.navigate_to_route_list()
