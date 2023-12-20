b = "17:52"
import datetime
def time(d):
    try:
        time_12h = datetime.datetime.strptime(d, "%I:%M")
        time_24h = time_12h.strftime("%H:%M")
        return time_24h
    except ValueError:
        try:
            time_24h = datetime.datetime.strptime(d, "%H:%M")
            time_12h = time_24h.strftime("%I:%M")
            return time_12h
        except ValueError:
            return None
convert12h = time(b)
print(f"{b} в 12 часовом формате {convert12h}")
print(f"{b} в 24 часовом формате {b}")