from turtle import Screen
from tkinter import Image, TclError
from draw_utils import *
from resources import *
from utils import *

try:
    wn = Screen()
    wn.tracer(0)
    wn.bgcolor("#fff6d2")
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
    textP.color("#23241f")

    while True:
        hour, minute, sec, ap = getSystemTime()
        drawHands(hour, minute, sec, handP)
        writeTime(hour, minute, sec, ap, textP)
        refreshScreen(wn, handP, textP)

except TclError:
    pass
