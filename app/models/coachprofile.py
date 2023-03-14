class CoachProfile:
    def __init__(self,username,fullname,language,yearsofexperience,picture):
        self.username = username
        self.fullname = fullname
        self.language = language
        self.yearsofexperience = yearsofexperience
        self.picture = picture

    def to_dict(self):
        return{
        'username': self.username,
        'fullname': self.fullname,
        'language': self.language,
        'yearsofexperience': self.yearsofexperience,
        'picture': self.picture,
        }
