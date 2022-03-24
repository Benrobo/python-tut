from datetime import datetime as date
import time

# Format date
def formatDate():
    currDate = date.now()
    year = currDate.year
    month = currDate.strftime("%B")
    day = currDate.strftime("%d")
    hr = currDate.strftime("%I")
    mint = currDate.strftime("%M")
    am = currDate.strftime("%p")
    return f"{month} {day}, {year} {hr}:{mint} {am}"
