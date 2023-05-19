import requests
from tkinter import *
from tkinter import ttk
from resources import century

response = requests.get("http://timeapi.io/api/TimeZone/AvailableTimeZones")
timezones = response.json()

root = Tk()
root.title("Timezone Finder")
root.geometry("400x400")
root.configure(bg="#fff6d2")
root.resizable(False, False)


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
    return zonesBox.get(ACTIVE)


title = Label(
    root, text="Timezone Search", font=(century, 14), fg="black", bg="#fff6d2"
)
title.pack(pady=20)

searchFrame = Frame(root)
searchFrame.pack()

filterLabel = Label(searchFrame, text="Filter ", font=(century, 10), bg="#fff6d2")
filterLabel.pack(side=LEFT)

searchBox = Entry(searchFrame, font=(century, 10), bg="#fffff0")
searchBox.pack(side=RIGHT)
searchBox.bind("<KeyRelease>", check)

boxFrame = Frame(root, height=50)
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

selectButton = Button(root, text="Select", command=select, fg="black", bg="#fffff0")
selectButton.pack()

update(timezones)

root.mainloop()
