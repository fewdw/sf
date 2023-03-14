class BoxerProfile:
    def __init__(self,username,fullname,age,weight,number_of_fights,feet,inches,language,years_of_experience,postal_code,picture):
        self.username = username
        self.fullname = fullname
        self.age = age
        self.weight = weight
        self.number_of_fights = number_of_fights
        self.feet = feet
        self.inches = inches
        self.language = language
        self.years_of_experience = years_of_experience
        self.postal_code = postal_code
        self.picture = picture
        

    def to_dict(self):
        return {
            "fullname": self.fullname,
            "Age": self.age,
            "Weight": self.weight,
            "numberoffights": self.number_of_fights,
            "feet":self.feet,
            "inches":self.inches,
            "language": self.language,
            "yearsofexperience": self.years_of_experience,
            "zipcode": self.postal_code,
            "picture": self.picture,
        }