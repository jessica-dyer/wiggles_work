from kivy.graphics import Rectangle, Color


def modified_bg_color(K, color_rgba_tuple=(1, .8, .8, 1)):
    colors_enabled = True

    class K2(K):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.previous_background_rect = None

        def draw_background_color(self):
            if self.canvas is None:
                return
            if self.previous_background_rect is not None:
                self.canvas.before.remove(self.previous_background_rect)
            self.canvas.before.add(Color(rgba=color_rgba_tuple))
            new_rect = Rectangle(pos=self.pos, size=self.size)
            self.canvas.before.add(new_rect)
            self.previous_background_rect = new_rect

        def on_width(self, widget, width):
            self.draw_background_color()

        def on_pos(self, widget, pos):
            self.draw_background_color()

    if colors_enabled:
        return K2
    else:
        return K
