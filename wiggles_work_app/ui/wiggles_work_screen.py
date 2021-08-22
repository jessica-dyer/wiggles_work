from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.gridlayout import GridLayout
from background_color_debugging import *

class AfterInitCaller(type(MDScreen)):
    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        obj.after_init()
        return obj

class WigglesWorkScreen(MDScreen, metaclass=AfterInitCaller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen_box_layout = BoxLayout(orientation='vertical')
        self.toolbar = MDToolbar(title="",
                                 elevation=8,
                                 pos_hint={'center_y': 1})
        self.screen_content = self.layout_for_screen_content()
        self.bottom_button_container = modified_bg_color(GridLayout)(rows=1,
                                                                     padding=8,
                                                                     spacing=15,
                                                                     pos_hint={'center_x': 0.5},
                                                                     size_hint=(None, None),
                                                                     size=(0, 80))

        self.screen_box_layout.add_widget(self.toolbar)
        self.screen_box_layout.add_widget(self.screen_content)
        self.screen_box_layout.add_widget(self.bottom_button_container)
        self.add_widget(self.screen_box_layout)


    def after_init(self):
        self.bottom_button_container.do_layout()
        self.bottom_button_container.width = self.bottom_button_container.minimum_width

    def layout_for_screen_content(self):
        return modified_bg_color(BoxLayout, (0, 1, 0, 1))(orientation='vertical',
                                                          spacing=10,
                                                          padding=(0, 10, 0, 10))
