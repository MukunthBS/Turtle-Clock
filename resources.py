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


def loadFont(path):
    p = ttf.TruetypeInfo(resource_path(path))
    name = p.get_name("name")
    p.close()
    add_file(resource_path(path))
    return name


eras = loadFont("ERASBD.TTF")
century = loadFont("CENTURY.TTF")
coprgtb = loadFont("COPRGTB.TTF")
coprgtl = loadFont("COPRGTL.TTF")

icon = resource_path("Clock.png")
