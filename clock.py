from turtle import Screen
from tkinter import Image, TclError
from draw_utils import *
from resources import *
from utils import *

try:
    wn = Screen()
    wn.tracer(0)
    wn.colormode(255)
    wn.bgcolor(255, 246, 210)
    wn.setup(width=600, height=600)
    wn.title("Clock")
    wn._root.resizable(False, False)

    img = Image("photo", file=icon)
    wn._root.iconphoto(True, img)

    drawStrap()

    drawFace()

    handP = makePen()

    textP = makePen()
    textP.up()
    textP.color(35, 36, 31)

    while True:
        hour, minute, sec, ap = getSystemTime()
        drawHands(hour, minute, sec, handP)
        writeTime(hour, minute, sec, ap, textP)
        refreshScreen(wn, handP, textP)

except TclError:
    pass
