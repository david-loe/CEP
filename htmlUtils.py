
from datetime import time

def getUnicodeClock(time):
    """
    Generates the closest Unicode Clock Symbol
    
    ...
    Parameters
    ----------
    time : datetime.time
        Time to be shown on the clock
    Returns
    --------
    clock : str
        A Unicode 6.0 string (symbol)
    """
    one_full = 0x0001F550
    one_half = 0x0001F55C

    if time.minute < 30:
        byte = one_full
    else:
        byte = one_half

    
    offsetHours =  ((time.hour % 12) - 1)
    if offsetHours == -1:
        offsetHours = 11

    return chr(byte + offsetHours)




    

