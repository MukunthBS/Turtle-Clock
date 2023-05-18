import turtle
import time
import tkinter
import os
import sys
import pyglet

try:

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    wn = turtle.Screen()
    wn.tracer(0)
    wn.colormode(255)
    wn.bgcolor(255, 246, 210)
    wn.setup(width=600, height=600)
    wn.title("Clock")
    wn._root.resizable(False, False)

    pyglet.font.add_file(resource_path("ERASBD.TTF"))
    pyglet.font.add_file(resource_path("COPRGTB.TTF"))
    pyglet.font.add_file(resource_path("COPRGTL.TTF"))
    pyglet.font.add_file(resource_path("CENTURY.TTF"))

    img = tkinter.Image("photo", file=resource_path("Clock.png"))
    wn._root.iconphoto(True, img)

    strapP = turtle.Turtle()
    strapP.hideturtle()
    strapP.color("black")
    strapP.speed(0)

    strapP.fillcolor(35, 36, 31)

    strapP.begin_fill()
    strapP.goto(-60, 0)
    strapP.setheading(90)
    strapP.forward(500)
    strapP.right(90)
    strapP.forward(120)
    strapP.right(90)
    strapP.forward(1000)
    strapP.right(90)
    strapP.forward(120)
    strapP.right(90)
    strapP.forward(500)
    strapP.end_fill()

    strapP.fillcolor(255, 246, 210)

    strapP.up()
    strapP.goto(0, -180)
    strapP.down()
    strapP.setheading(180)
    strapP.begin_fill()
    strapP.circle(5)
    strapP.end_fill()

    strapP.up()
    strapP.goto(0, -220)
    strapP.down()
    strapP.setheading(180)
    strapP.begin_fill()
    strapP.circle(5)
    strapP.end_fill()

    strapP.up()
    strapP.goto(0, -260)
    strapP.down()
    strapP.setheading(180)
    strapP.begin_fill()
    strapP.circle(5)
    strapP.end_fill()

    def drawFace():
        faceP = turtle.Turtle()
        faceP.hideturtle()
        faceP.color("black")
        faceP.speed(0)

        faceP.width(3)
        faceP.up()
        faceP.goto(0, 100)
        faceP.setheading(180)
        faceP.down()
        faceP.fillcolor(88, 124, 119)
        faceP.begin_fill()
        faceP.circle(100)
        faceP.end_fill()

        faceP.width(2)
        for i in range(0, 360, 30):
            faceP.up()
            faceP.goto(0, 0)
            faceP.setheading(i)
            faceP.forward(87)
            faceP.down()
            faceP.forward(13)

        faceP.width(1)
        for i in range(0, 360, 6):
            if i % 5 == 0:
                continue
            faceP.up()
            faceP.goto(0, 0)
            faceP.setheading(i)
            faceP.forward(94)
            faceP.down()
            faceP.forward(6)

        faceP.up()
        faceP.goto(0, 60)
        faceP.write("=T=", align="center", font=("Eras Bold ITC", 5, "italic"))
        faceP.goto(0, 45)
        faceP.write("TIME", align="center", font=("Century", 5, "normal"))

    drawFace()

    handP = turtle.Turtle()
    handP.hideturtle()
    handP.speed(0)

    def drawHands(hour, minute, sec, handP):
        handP.up()
        handP.goto(0, 0)
        handP.setheading(90)
        handP.right(hour / 12 * 360)
        handP.width(3)
        handP.color(0, 0, 0)
        handP.down()
        handP.forward(40)

        handP.up()
        handP.goto(0, 0)
        handP.setheading(90)
        handP.right(minute / 60 * 360)
        handP.width(2)
        handP.color(15, 15, 15)
        handP.down()
        handP.forward(60)

        handP.up()
        handP.goto(0, 0)
        handP.setheading(90)
        handP.right(sec / 60 * 360)
        handP.width(1)
        handP.color(30, 30, 30)
        handP.down()
        handP.forward(80)

    textP = turtle.Turtle()
    textP.hideturtle()
    textP.speed(0)
    textP.up()
    textP.color(35, 36, 31)

    while True:
        hour = int(time.strftime("%I"))
        minute = int(time.strftime("%M"))
        sec = int(time.strftime("%S"))
        ap = time.strftime("%p")
        drawHands(hour, minute, sec, handP)
        textP.goto(-200, 77)
        textP.write(
            str(hour).rjust(2, "0"),
            align="center",
            font=("Copperplate Gothic Light", 48, "normal"),
        )
        textP.goto(-200, 36)
        textP.write(
            ". .",
            align="center",
            font=("Copperplate Gothic Light", 48, "normal"),
        )
        textP.goto(-200, -48)
        textP.write(
            str(minute).rjust(2, "0"),
            align="center",
            font=("Copperplate Gothic Light", 48, "normal"),
        )
        textP.goto(-200, -89)
        textP.write(
            ". .",
            align="center",
            font=("Copperplate Gothic Light", 48, "normal"),
        )
        textP.goto(-200, -173)
        textP.write(
            str(sec).rjust(2, "0"),
            align="center",
            font=("Copperplate Gothic Light", 48, "normal"),
        )
        textP.goto(200, 0)
        textP.write(
            ap[0],
            align="center",
            font=("Copperplate Gothic Bold", 64, "normal"),
        )
        textP.goto(200, -100)
        textP.write(
            ap[1],
            align="center",
            font=("Copperplate Gothic Bold", 64, "normal"),
        )
        wn.update()
        time.sleep(1)
        handP.clear()
        textP.clear()
except tkinter.TclError:
    pass
