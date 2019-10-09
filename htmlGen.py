from settings import Settings as set
from ical import *
from yattag import Doc


eventDaysList = getEventList()
count_days = len(eventDaysList)
pdfsize = set.paperformats[set.ratio]

doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')

with tag('html'):
    with tag('head'):
        with tag('style'):
            doc.asis('''@page {
		    	    size: '''+ pdfsize +''' landscape;
		            margin: 2cm;
		            }''')
        doc.asis('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
    with tag('body'):
        with tag('div', klass='container'):
            with tag('h1', align = "center"):
                text('Terminübersicht')
            with tag('div', klass='row justify-content-around'):
                for day in eventDaysList:
                    with tag('div',klass= 'col',  width = '30%'):
                        for event in day:
                            with tag('h3'):
                                text(event.summary)
                            with tag('p'):
                                text(event.start.strftime('%H:%M') + ' - ' + event.end.strftime('%H:%M'))


file = open('index.HTML', 'w')
file.write(doc.getvalue())
file.close()

