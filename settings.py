from dateutil.relativedelta import *

class Settings:
    """Here you can set your standard settings"""
    path_calendar = "https://calendar.google.com/calendar/ical/jcg.stadtoldendorf%40gmail.com/public/basic.ics"
    day_range = relativedelta(months=0, days=7)
    staringpoint = relativedelta(months=0, days=0, hours=2, minutes=0) # time from where on to look for events (today + startingpoint)
    weekdays = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
    #ratios = {"16:9" : (16,9), "4:3" : (4,3), "A4": (210,297)}
    paperformats = {"16:9": "B0", "4:3":"B1","A4":"A4"}
    ratio = "4:3"
    path_background = "" #if no background is used: ""
    path_qrcode = "" #if no qr-code is used: ""
    path_logo = "" #if no logo is used: ""
    path_htmlOutput = ""
    path_output = ""
    name_output = ""


