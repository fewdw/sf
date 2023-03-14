class Event:
    def __init__(self,coach,gym,address,date,readable_date,language,rules,picture,max_attendees):
        self.coach = coach
        self.gym = gym
        self.address = address
        self.date = date
        self.readable_date = readable_date
        self.language = language
        self.rules = rules
        self.picture = picture
        self.max_attendees = max_attendees

    def to_dict(self):
        return {
            "coach": self.coach,
            "gym": self.gym,
            "address": self.address,
            "boxers": [],
            "waiting_list":[],
            "max_attendees":self.max_attendees,
            "date":self.date,
            "readable_date":self.readable_date,
            "language": self.language,
            "rules": self.rules,
            'picture':self.picture
        }