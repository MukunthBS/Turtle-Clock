from turtle import Screen
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import time
import requests
from draw_utils import *
from resources import *
from idlelib.tooltip import Hovertip


wn = Screen()
wn.tracer(0)
wn.bgcolor("#fff6d2")
wn.setup(width=600, height=600)
wn.title("World Watch")
root = wn._root
root.resizable(False, False)

timeZone = ""


def getTimeZone():
    global root
    response = requests.get("http://timeapi.io/api/TimeZone/AvailableTimeZones")
    timezones = response.json()

    zoneRoot = Toplevel(root)
    zoneRoot.title("Timezone Finder")
    zoneRoot.geometry("400x400")
    zoneRoot.configure(bg="#fff6d2")
    zoneRoot.resizable(False, False)
    zoneRoot.transient(root)
    zoneRoot.grab_set()

    def update(data):
        zonesBox.delete(0, END)
        if data != []:
            for item in data:
                zonesBox.insert(END, item)
            zonesBox.select_set(0)

    def check(event):
        typed = searchBox.get()
        if typed == "":
            data = timezones
        else:
            data = []
            for item in timezones:
                if typed.lower() in item.lower():
                    data.append(item)
        update(data)

    def select():
        global timeZone
        timeZone = zonesBox.get(ACTIVE)
        zoneRoot.grab_release()
        zoneRoot.destroy()

    title = Label(
        zoneRoot, text="Timezone Search", font=(century, 14), fg="black", bg="#fff6d2"
    )
    title.pack(pady=20)

    searchFrame = Frame(zoneRoot)
    searchFrame.pack()

    filterLabel = Label(searchFrame, text="Filter ", font=(century, 10), bg="#fff6d2")
    filterLabel.pack(side=LEFT)

    searchBox = Entry(searchFrame, font=(century, 10), bg="#fffff0")
    searchBox.pack(side=RIGHT)
    searchBox.bind("<KeyRelease>", check)

    boxFrame = Frame(zoneRoot, height=50)
    boxFrame.pack(pady=40)

    zonesBox = Listbox(boxFrame, width=40, bg="#fffff0")
    zonesBox.pack(side=LEFT)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Vertical.TScrollbar", background="#fff6d2")

    scrollbar = ttk.Scrollbar(boxFrame, orient="vertical", style="Vertical.TScrollbar")
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=zonesBox.yview)

    zonesBox.config(yscrollcommand=scrollbar.set)

    selectButton = Button(
        zoneRoot, text="Select", command=select, fg="black", bg="#fffff0"
    )
    selectButton.pack()

    update(timezones)
    root.wait_window(zoneRoot)
    return timeZone


def switchTimeMode(timeMode):
    global timeZone
    global worldButton
    global systemButton
    if timeMode == "world":
        timeZone = getTimeZone()
        if timeZone == None:
            timeZone = ""
        else:
            systemButton["state"] = NORMAL

    else:
        timeMode = "sys"
        timeZone = ""
        systemButton["state"] = DISABLED


def getTime(timeZone):
    if timeZone == "":
        hour, minute, sec, ap = getSystemTime()
    else:
        hour, minute, sec, ap = getWorldTime(timeZone)
    return hour, minute, sec, ap


def getSystemTime():
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    ap = time.strftime("%p")
    return hour, minute, sec, ap


def refreshScreen(wn, handP, textP, timeZone):
    wn.update()
    if timeZone == "":
        time.sleep(1)
    else:
        time.sleep(0.1)
    handP.clear()
    textP.clear()


def getWorldTime(timezone):
    try:
        timeResponse = requests.get(
            "http://timeapi.io/api/Time/current/zone?timeZone=" + timezone
        )
        curr = timeResponse.json()
        hour = curr["hour"]
        minute = curr["minute"]
        sec = curr["seconds"]
        ap = "AM"
        if hour > 12:
            hour = hour - 12
            ap = "PM"
        elif hour == 12:
            ap = "PM"
        elif hour == 0:
            hour = 12
        return hour, minute, sec, ap
    except:
        messagebox.showerror("Connection Error", "Connection couldn't be established!")


try:
    img = PhotoImage("photo", file=icon)
    root.iconphoto(True, img)

    drawStrap()

    drawFace()

    handP = makePen()

    textP = makePen()
    textP.up()
    textP.color("#23241f")

    buttonFrame = Frame(root)
    buttonFrame.pack(side=RIGHT)

    worldPic = PhotoImage(file=world)
    monitorPic = PhotoImage(file=monitor)

    worldButton = Button(
        root,
        text="World",
        image=worldPic,
        bg="#fff6d2",
        command=lambda timeMode="world": switchTimeMode(timeMode),
        cursor="hand2",
        borderwidth=0,
    )
    worldButton.pack()
    worldButton.place(x=550, y=550)
    worldTip = Hovertip(worldButton, "World Clock")

    systemButton = Button(
        root,
        text="System",
        image=monitorPic,
        bg="#fff6d2",
        state=DISABLED,
        command=lambda timeMode="sys": switchTimeMode(timeMode),
        cursor="hand2",
        borderwidth=0,
    )
    systemButton.pack()
    systemButton.place(x=500, y=550)
    systemTip = Hovertip(systemButton, "Use System Time")

    while True:
        hour, minute, sec, ap = getTime(timeZone)
        drawHands(hour, minute, sec, handP)
        writeTime(hour, minute, sec, ap, textP)
        refreshScreen(wn, handP, textP, timeZone)

except TclError:
    pass
