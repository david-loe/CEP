from dateutil.relativedelta import relativedelta

class Settings:
    """
    A class used to set general Settings

    ...

    Attributes
    ----------
    path_calendar : str
        path to ICS-File of your calendar
    day_range : relativedelta
        timerange covered by the Event Presentation
    staringpoint : relativedelta
        time from where on to look for events (today + startingpoint)
    weekdays : list
        customizable weekday names
    output_width : int
        width of the Output
    output_height  int
        height of the Output
    output_ratio : list
        a list of [output_width,output_height]
    path_background : str
        path to the background image - if empty no background image used
    path_qrcode : str
        path to  qr-code - if empty no qr-code is used
    path_logo : str
        path to logo image - if empty no logo image is used
    path_htmlOutput : str
        path for HTML Output
    path_output : str
        folder for the outputs
    name_output : str
        name of the output files (without file extention)
    text_title : str
        Title of the Event Presentation
    body_style : str
        Style of the HTML body
    heading_style : str
        Style of the Heading
    
    """
    path_calendar = "" # URL to ICS-File of your calendar
    day_range = relativedelta(months=0, days=7) # timerange covered by the Event Presentation
    staringpoint = relativedelta(months=0, days=0, hours=2, minutes=0) # time from where on to look for events (today + startingpoint)
    weekdays = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"]
    output_width = 16
    output_height = 10
    output_ratio = [output_width, output_height]
    path_background = "" #if no background is used: ""
    path_qrcode = "" #if no qr-code is used: ""
    path_logo = "" #if no logo is used: ""
    path_htmlOutput = "index.HTML"
    path_output = ""
    name_output = "Terminuebersicht"
    text_title = "Wochenübersicht" # Title of the Event Presentation
    body_style = "bg-dark"
    heading_style = "text-white"


