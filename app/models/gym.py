class Gym:
    def __init__(self, username, name, phone, address, language, description, picture):
        self.username = username
        self.name = name
        self.phone = phone
        self.address = address
        self.language = language
        self.description = description
        self.picture = picture

    def to_dict(self):
        return {
            'username':self.username,
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'language': self.language,
            'description': self.description,
            'picture': self.picture,
            'uniqueboxers':0,
            'events':[],
            'rating':[]
        }