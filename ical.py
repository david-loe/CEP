# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:58:11 2019

@author: David
"""
import codecs
from dateutil.parser import *
from datetime import *
from icalevents.icalevents import events
from dateutil.relativedelta import *
import os

#CONSTANTS
weekdays=["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
days_to_look = 7
today = datetime.today()


def gen_flyer():
    """
    Add additional pages for all pictures in the 'pics' folder
    """
    from os import listdir
    from os.path import isfile, join
    pics = [f for f in listdir(os.path.realpath(__file__) + "\\..\\pics") if isfile(join(os.path.realpath(__file__) + "\\..\\pics", f))]
    strings= []
    for pic in pics:
        strings.append("""
                       \\begin{frame}
\\hspace*{-29}%
\\includegraphics[width=\\paperwidth,width=\\paperwidth]{pics/""" + pic + """}

\\setbeamercolor{footline}{bg=black, fg=lightgray}
\\setbeamerfont{footline}{size=6pt}
\\begin{beamercolorbox}[wd=\\paperwidth, dp=\\paperheight]{footline}%
	\\\\
	www.jesus-christus-gemeinde.de/veranstaltungen
	\\begin{wrapfigure}{r}{0.2\\textwidth}
		\\vspace{-33pt}
		\\includegraphics[width=0.2\\textwidth]{Termine.pdf}
\\end{wrapfigure}\\end{beamercolorbox}%
\\end{frame}
                       """)
    return "".join(strings)
def gen_pdf(tex, name):
    """
    Generates the pdf from string
    """
    import subprocess
    

    f = codecs.open(name + '.tex','w','utf-8') 
    f.write(tex)
    f.close()

    proc=subprocess.Popen(['pdflatex','Termin_Uebersicht.tex'])
    #subprocess.Popen(['pdflatex',tex])
    proc.communicate()
    #os.unlink(name +'.tex')
    os.unlink(name +'.log')
    os.unlink(name +'.aux')
    os.unlink(name +'.out')
    os.unlink(name +'.nav')
    os.unlink(name +'.toc')
    os.unlink(name +'.snm')
    proc.terminate()

def gen_eventdaylist(eventlist,event_limit=2, space_between = 10, space_after_line = 5):
    """
    Generates the Eventlist for one Box

   :param list eventlist: The list of events displayed in a Box
   :param event_limit: The Limit of Events displayed in a Box
   :param event_limit: integer or None
   :param space_between: Spacing between lines (default=10)
   :type space_between: integer or None
   :param space_after_line: Spacing after the Eventend line (default=5)
   :type space_after_line: integer or None
   :return: latex text to generate the box
   :rtype: str
   """
    space_above = "-0.23\\textwidth-"
    shift = 0
    strings = []
    for event in eventlist:
        tempstrs = []
        if shift != 0:
            tempstrs.append("""
		                   \\node[align=center,below,yshift=""" + space_above + str (shift) + """] (sep1) at (current bounding box.north) {\\rule{0.83\\textwidth}{0.8pt}};""")
            shift+=space_after_line
        if event.summary.find(" ") != -1:
            summarys = event.summary.split(" ")
            for summary in summarys:
                tempstrs.append("""
                             \\node[align=center,below,yshift=""" + space_above + str (shift) + """] (summary1) at (current bounding box.north) {\\textbf{""" + summary + """}};""")
                shift += space_between
        else:
            tempstrs.append("""
                         \\node[align=center,below,yshift=""" + space_above + str (shift) + """] (summary1) at (current bounding box.north) {\\textbf{""" + event.summary + """}};""")
            shift += space_between
        tempstrs.append("""
		\\node[align=center,below,yshift=""" + space_above + str (shift) + """] (time1) at (current bounding box.north) {""" + event.start.strftime("%H:%M") + """ Uhr};""")
        shift+=space_between
        if shift > (space_between*3+space_after_line)*event_limit:
            break
        strings = strings + tempstrs
        
    return "".join(strings)



class CEST(tzinfo):
     def utcoffset(self, dt):
       return timedelta(hours=2)
     def dst(self, dt):
         return timedelta(0)
     def tzname(self,dt):
         return "Europe/Berlin"
     
class CET(tzinfo):
     def utcoffset(self, dt):
       return timedelta(hours=1)
     def dst(self, dt):
         return timedelta(0)
     def tzname(self,dt):
         return "Europe/Berlin"
     
#get summertime
last_SU_march=today+relativedelta(month=3,day=31,hour=2,minute=0,second=0, weekday=SU(-1))
last_SU_oct=today+relativedelta(month=10,day=31,hour=3,minute=0,second=0, weekday=SU(-1))
if (today < last_SU_march) or (today > last_SU_oct):
    timezone=CET()
else:
    timezone=CEST()

def normtz(date):
    """
    Normilizes the timezone of the event

   :param datetime date: The date to normilize
   :return: normilized Datetime
   :rtype: datetime
   """
    if date.tzinfo.tzname(date) == "UTC":
        date = date.replace(tzinfo=timezone)
        date = date + timezone.utcoffset(date)
    return date


es  = events(url = "https://calendar.google.com/calendar/ical/jcg.stadtoldendorf%40gmail.com/public/basic.ics", start=today+relativedelta(hours=+2), end=today+relativedelta(days=+days_to_look))
#fix TimeZone Bug
for event in es:
    event.start = normtz(event.start)
    event.end = normtz(event.end)
    
es.sort()
events = [[]]
cache_date = today.date()
cache_int = 0



for event in es:
    if event.start.date() == cache_date:
        events[cache_int].append(event)
    elif events[0] == []:
        events[cache_int].append(event)
        cache_date = event.start.date()
    else:
        cache_int += 1
        events.append([])
        events[cache_int].append(event)
        cache_date = event.start.date()


# latex generation

latex = []
latex.append("""
\\documentclass{beamer}
\\usepackage[utf8]{inputenc}
\\usepackage{float}
\\usepackage{wrapfig}
\\usepackage{tikz}


\\title{Termine}
\\author{David Löwens}
\\date{\\today}


% Color definition
\\definecolor{lightgray}{RGB}{190,190,190}
\\definecolor{jcgblue}{RGB}{40,106,166}
\\definecolor{jcgred}{RGB}{171,36,48}

% Title Color
\\setbeamertemplate{frametitle}[default][center]
\\setbeamercolor{frametitle}{fg=black}
\\setbeamerfont{frametitle}{size={\\fontsize{28}{16}}}
\\setbeamercolor{daycaption}{fg=white, bg=gray}
\\setbeamercolor{background}{bg=white}

% disable navigation symbols 
\\setbeamertemplate{navigation symbols}{}




\\begin{document}
{\\usebackgroundtemplate{\\includegraphics[width=\\paperwidth]{background_white.pdf}}
\\begin{frame}[t] %%Eine Folie
	\\frametitle{Termine} %%Folientitel
	\\begin{columns}[T]""")


if(len(events)<3):
    for eventlist in events:
        latex.append("""
        \\fontsize{13pt}{9pt}
        \\begin{column}{0.4\\textwidth}
		\\begin{tikzpicture}
		\\node[] (image) at (0,0) {\\includegraphics[width=\\textwidth]{colorbox.pdf}};
		\\node[below right,white,yshift=-4,xshift=2] (text) at (current bounding box.north west) {\\textbf{"""+ weekdays[eventlist[0].start.weekday()] +", "+ eventlist[0].start.strftime("%d.%m") + """}};""")
        latex.append(gen_eventdaylist(eventlist, space_between=13))
        latex.append("""
        \\end{tikzpicture}
		\\end{column}""")
else:
    for i in range(3):
        latex.append("""
        \\fontsize{10pt}{9pt}
        \\begin{column}{0.3\\textwidth}
		\\begin{tikzpicture}
		\\node[] (image) at (0,0) {\\includegraphics[width=\\textwidth]{colorbox.pdf}};
		\\node[below right,white,yshift=-4,xshift=2] (text) at (current bounding box.north west) {\\textbf{"""+ weekdays[events[i][0].start.weekday()] +", "+ events[i][0].start.strftime("%d.%m") + """}};""")
        latex.append(gen_eventdaylist(events[i]))
        latex.append("""
                     \\end{tikzpicture}""")
        if len(events)>i+3:
            latex.append("""
            \\begin{tikzpicture}
		    \\node[] (image) at (0,0) {\\includegraphics[width=\\textwidth]{colorbox.pdf}};
		    \\node[below right,white,yshift=-4,xshift=2] (text) at (current bounding box.north west) {\\textbf{"""+ weekdays[events[i+3][0].start.weekday()] +", "+ events[i+3][0].start.strftime("%d.%m") + """}};""")
            latex.append(gen_eventdaylist(events[i+3]))
            latex.append("""
            \\end{tikzpicture}""")
        latex.append("""
		\\end{column}""")
latex.append("""
             \\end{columns}
		\\setbeamercolor{footline}{bg=black, fg=lightgray}
		\\setbeamerfont{footline}{size=6pt}
		\\begin{beamercolorbox}[wd=\\paperwidth, dp=\\paperheight]{footline}%
			\\\\
			www.jesus-christus-gemeinde.de/veranstaltungen""")
if len(events) < 6:
    latex.append("""
	\\begin{wrapfigure}{r}{0.2\\textwidth}""")
    if len(events) < 4:
        latex.append("""
            \\vspace{-33pt}""")
    else:
        latex.append("""
            \\vspace{-75pt}""")
    latex.append("""
                 \\includegraphics[width=0.2\\textwidth]{Termine.pdf}
                 \\end{wrapfigure}""")
latex.append("""\\end{beamercolorbox}%
\\end{frame}
}""")
#latex.append(gen_flyer())
latex.append("""\\end{document}""")





document = "".join(latex)

gen_pdf(document, "Termin_Uebersicht")
