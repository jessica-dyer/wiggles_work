from kivy.graphics import Color
from kivy.utils import get_color_from_hex

# def make_color(hex_code, alpha_in_percent):
#     alpha_in_int = int(alpha_in_percent * 255)
#     alpha_in_hex = hex(alpha_in_int)
#     alpha_in_hex = alpha_in_hex[2:4]
#     complete_hex_code = hex_code + alpha_in_hex
#     return Color(get_color_from_hex(complete_hex_code))

def make_color(hex_code, alpha_in_percent):
    r_hex = hex_code[0:2]
    g_hex = hex_code[2:4]
    b_hex = hex_code[4:6]
    r = int(r_hex, 16) / 255
    g = int(g_hex, 16) / 255
    b = int(b_hex, 16) / 255
    return Color(r, g, b, alpha_in_percent)


class WWColors:
    #ROW_CLICK_HIGHLIGHT = make_color("d8f3dc", 0.9)
    #ROW_CLICK_HIGHLIGHT  = Color(get_color_from_hex("d8f3dcff"))
    #ROW_CLICK_HIGHLIGHT_STUPID = Color(0.847, 0.953, 0.863, 1)
    #ROW_CLICK_HIGHLIGHT = Color(0, 1, 0, 1)
    #ROW_CLICK_HIGHLIGHT = make_color("00FF00", 1)
    ROW_CLICK_HIGHLIGHT = make_color("d8f3dc", .75)



