from datetime import datetime

class DateTimeChecker:
    
    def __init__(self):
        pass

    def is_date_later_than_current_time(self,date_string):
        date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M')
        return date > datetime.now()
    
    def date_to_readable_format(self,date_string):
        date_time_obj = datetime.strptime(date_string, '%Y-%m-%dT%H:%M')
        formatted_date = date_time_obj.strftime('%B %d %Y, %I:%M %p')
        return formatted_date
