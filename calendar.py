from dateutil.parser import *
from datetime import *
from icalevents.icalevents import events
from settings import Settings as set
from timezone import *

def getEventList():
    
    today = datetime.today()
    #
    icalEvents  = events(url = set.path_calendar, start = today + set.staringpoint, end = today + set.day_range)
    
    #fix TimeZone Bug
    for event in icalEvents:
        event.start = normalizeTimezone(event.start, getTimezone(event.start))
        event.end = normalizeTimezone(event.end, getTimezone(event.end))
    
    
    icalEvents.sort()
    eventDaysList = [[]]
    cache_date = today.date()
    cache_int = 0
    
    for event in icalEvents:
        if event.start.date() == cache_date:
            eventDaysList[cache_int].append(event)
        elif eventDaysList[0] == []:
            eventDaysList[cache_int].append(event)
            cache_date = event.start.date()
        else:
            cache_int += 1
            eventDaysList.append([])
            eventDaysList[cache_int].append(event)
            cache_date = event.start.date()
    return eventDaysList