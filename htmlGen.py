from settings import Settings as set
from ical import getEventList
from htmlUtils import getUnicodeClock
from yattag import Doc, indent


eventDaysList = getEventList()
count_days = len(eventDaysList)

doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')

# HTML Head
with tag('html'):
    with tag('head'):
        doc.asis('<meta name="description" content="' + set.text_title + '" charset="utf-8">')
        doc.asis('<link rel="stylesheet" href="bootstrap.css">')
    with tag('body', klass=set.body_style):
        with tag('div', klass='container'):
            # Headline
            with tag('div', klass='row justify-content-center mb-5'):
                with tag('div', klass='col-auto'):
                    with tag('h1', klass=set.heading_style):
                        text(set.text_title)
            # Events
            with tag('div', klass='row justify-content-around'):
                for day in eventDaysList:
                    with tag('div',klass= 'col-4'):
                        with tag('div', klass='card', style='display: block; width: 100%'):
                            with tag('div', klass='card-header'):
                                with tag('h2', klass='text-nowrap'):
                                    with tag('span', klass='float-left'):
                                        text(set.weekdays[day[0].start.weekday()])
                                    with tag('span', klass='float-right font-weight-light'):
                                        text(day[0].start.strftime('%d.%m'))
                                    doc.asis('<br>')
                            with tag('div', klass='card-body'):
                                first = True
                                for event in day:
                                    if not first:
                                        doc.asis('<hr/>')
                                    else:
                                        first = False
                                    with tag('h3', klass='card-title text-center font-weight-bold'):
                                        text(event.summary)
                                    with tag('h4', klass='card-text text-center'):
                                        text(getUnicodeClock(event.start) + ' ' + event.start.strftime('%H:%M') + ' Uhr')
                        doc.asis('<br>') 
                                    

# Saving the HTML-File to path_htmlOutput
file = open(set.path_htmlOutput, 'w', encoding='utf8')
file.write(indent(doc.getvalue()))
file.close()

