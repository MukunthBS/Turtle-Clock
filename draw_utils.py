import turtle
from resources import *


def makePen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    return pen


def drawFace():
    faceP = makePen()
    faceP.color("black")
    faceP.width(3)
    faceP.up()
    faceP.goto(0, 100)
    faceP.setheading(180)
    faceP.down()
    faceP.fillcolor("#587c77")
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
    faceP.write("=T=", align="center", font=(eras, 5, "italic"))
    faceP.goto(0, 45)
    faceP.write("TIME", align="center", font=(century, 5, "normal"))


def drawStrap():
    strapP = makePen()
    strapP.color("black")
    strapP.fillcolor("#23241f")

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

    strapP.fillcolor("#fff6d2")

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


def drawHands(hour, minute, sec, handP):
    handP.up()
    handP.goto(0, 0)
    handP.setheading(90)
    handP.right(hour / 12 * 360)
    handP.width(3)
    handP.color("black")
    handP.down()
    handP.forward(40)

    handP.up()
    handP.goto(0, 0)
    handP.setheading(90)
    handP.right(minute / 60 * 360)
    handP.width(2)
    handP.color("#0f0f0f")
    handP.down()
    handP.forward(60)

    handP.up()
    handP.goto(0, 0)
    handP.setheading(90)
    handP.right(sec / 60 * 360)
    handP.width(1)
    handP.color("#1e1e1e")
    handP.down()
    handP.forward(80)


def writeTime(hour, minute, sec, ap, textP):
    textP.goto(-200, 77)
    textP.write(
        str(hour).rjust(2, "0"),
        align="center",
        font=(coprgtl, 48, "normal"),
    )
    textP.goto(-200, 36)
    textP.write(
        ". .",
        align="center",
        font=(coprgtl, 48, "normal"),
    )
    textP.goto(-200, -48)
    textP.write(
        str(minute).rjust(2, "0"),
        align="center",
        font=(coprgtl, 48, "normal"),
    )
    textP.goto(-200, -89)
    textP.write(
        ". .",
        align="center",
        font=(coprgtl, 48, "normal"),
    )
    textP.goto(-200, -173)
    textP.write(
        str(sec).rjust(2, "0"),
        align="center",
        font=(coprgtl, 48, "normal"),
    )
    textP.goto(200, 0)
    textP.write(
        ap[0],
        align="center",
        font=(coprgtb, 64, "normal"),
    )
    textP.goto(200, -100)
    textP.write(
        ap[1],
        align="center",
        font=(coprgtb, 64, "normal"),
    )
