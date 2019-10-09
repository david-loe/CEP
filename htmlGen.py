from settings import Settings as set
from ical import *
from yattag import Doc


#eventDaysList = getEventList()
#count_days = len(eventDaysList)

doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')

with tag('html'):
    with tag('head'):
        doc.asis('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
    with tag('body'):
#        with tag('div', style = "width: " +  str(set.resolution[0]) + "mm; height: " + str(set.resolution[1]) + "mm; background: 'light grey';"):
            with tag('h1'):
                text('Terminübersicht')
            with tag('p'):
                text('Hier könnte ihre Werbung stehen')


file = open('index.HTML', 'w')
file.write(doc.getvalue())
file.close()

print(set.ratios[set.ratio])
