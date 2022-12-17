import winsound


def makeBeep():
    frequency = 800
    duration = 500
    winsound.Beep(frequency, duration)
