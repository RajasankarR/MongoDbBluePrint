
from datetime import date

class User(object):
	def __init__(self,name,lastname):
		self.name=name
		self.lastname=lastname
	
	def __repr__(self):
		return f"<User {self.name}>"	