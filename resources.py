import os
import sys
from pyglet import options
from pyglet.font import add_file, ttf

options["win32_gdi_font"] = True


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_font(path):
    p = ttf.TruetypeInfo(resource_path(path))
    name = p.get_name("name")
    p.close()
    add_file(resource_path(path))
    return name


eras = load_font("ERASBD.TTF")
century = load_font("CENTURY.TTF")
coprgtb = load_font("COPRGTB.TTF")
coprgtl = load_font("COPRGTL.TTF")

icon = resource_path("Clock.png")
