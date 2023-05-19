import time


def getSystemTime():
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    ap = time.strftime("%p")
    return hour, minute, sec, ap


def refreshScreen(wn, handP, textP):
    wn.update()
    time.sleep(1)
    handP.clear()
    textP.clear()
