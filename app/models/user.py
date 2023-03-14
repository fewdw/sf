class User:
	def __init__(self,username,password,role,language):
		self.username = username
		self.password = password
		self.role = role
		self.language = language

	def to_dict(self):
		return {
			"username": self.username,
			"password": self.password,
			"role": self.role,
			"language": self.language
		}