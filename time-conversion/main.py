import datetime


def timeConversion(s):
    time = datetime.datetime.strptime(s, "%I:%M:%S%p")
    return time.strftime("%H:%M:%S")
