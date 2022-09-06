import datetime
gigasecond = datetime.timedelta(seconds = 1000000000)
def add(moment):
    """
    Function that determines the date and time after a gigasecond (10^9 seconds) has passed
    given a moment
    :param moment: datetime object
    :returnt: datetime
    
    """
    return moment + gigasecond
