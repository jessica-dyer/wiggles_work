from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.gridlayout import GridLayout


class WigglesWorkScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen_box_layout = BoxLayout(orientation='vertical')
        self.toolbar = MDToolbar(title="",
                                 elevation=8,
                                 pos_hint={'center_y': 1})
        self.screen_content = BoxLayout(orientation='vertical')
        self.bottom_button_container = GridLayout(rows=1,
                                                  padding=8,
                                                  spacing=15,
                                                  pos_hint={'center_x': 0.5},
                                                  size_hint=(None, None),
                                                  size=(0, 80))

        self.screen_box_layout.add_widget(self.toolbar)
        self.screen_box_layout.add_widget(self.screen_content)
        self.screen_box_layout.add_widget(self.bottom_button_container)
        self.add_widget(self.screen_box_layout)

    def on_pre_enter(self, *args):
        super().on_pre_enter(args)
        self.bottom_button_container.do_layout()
        self.bottom_button_container.width = self.bottom_button_container.minimum_width

