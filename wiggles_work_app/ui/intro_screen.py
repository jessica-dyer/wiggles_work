import kivy
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton


class IntroductionScreen(MDScreen):
    def __init__(self, wiggles_work_app, **kwargs):
        super().__init__(**kwargs)

        self.wiggles_work_app = wiggles_work_app
        self.screen_box_layout = BoxLayout(orientation='vertical',
                                           # adaptive_height=True,
                                           spacing=80,
                                           padding=30,
                                           pos_hint={'center_x':0.5})

        self.username = MDTextField(hint_text="Username",
                                    mode='fill')
        self.password = MDTextField(hint_text="Password",
                                    mode='fill')
        self.enter_button = MDRectangleFlatButton(text="Play!")
        self.enter_button.bind(on_press=self.on_click_enter)

        self.screen_box_layout.add_widget(self.username)
        self.screen_box_layout.add_widget(self.password)
        self.screen_box_layout.add_widget(self.enter_button)
        self.add_widget(self.screen_box_layout)


    def on_click_enter(self, button):
        self.wiggles_work_app.navigate_to_route_list()