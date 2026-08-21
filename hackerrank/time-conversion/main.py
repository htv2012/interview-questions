import datetime


def timeConversion(s):
    time = datetime.datetime.strptime(s, "%I:%M:%S%p")  # noqa: DTZ007
    return time.strftime("%H:%M:%S")
