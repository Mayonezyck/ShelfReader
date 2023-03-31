# this class of student represents each studnet object that is unique

class Student:
	def __init__(self):
		self.ID = '00000000'
		self.isStaff = False

	def __str__(self):
		return str(self.ID)
	
	def getID(self):
		return self.ID

