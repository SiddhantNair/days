from datetime import datetime

def fromDate(date):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    date = datetime.strptime(date, '%d %m %Y').weekday()
    return days[date]

def bleh(list):
    meow = sum(list)
    return meow