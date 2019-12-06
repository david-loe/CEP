from dateutil.relativedelta import relativedelta
from dateutil.rrule import SU
from datetime import tzinfo, timedelta

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
     
def getTimezone(date):
    """
    Returns the timezone of a date

    ...
    Parameters
    ----------
    datetime : date
        The date to check
    
    Returns
    -------
    datetime.tzinfo
        timezone
    """
    last_SU_march = date + relativedelta(month=3,day=31,hour=2,minute=0,second=0, weekday=SU(-1))
    last_SU_oct = date + relativedelta(month=10,day=31,hour=3,minute=0,second=0, weekday=SU(-1))
    if (date < last_SU_march) or (date > last_SU_oct):
        return CET()
    else:
        return CEST()

def normalizeTimezone(date,timezone):
    """
    Normalizes the timezone of the event

    ...
    Parameters
    ---------
    datetime : date
        The date to normalize
    tzinfo : timezone
        The timezone to normalize to

    Returns
    -------
    datetime
        normalized Datetime
    
    """
    if date.tzinfo.tzname(date) == "UTC":
        date = date.replace(tzinfo=timezone)
        date = date + timezone.utcoffset(date)
    return date