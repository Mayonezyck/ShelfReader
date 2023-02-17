# this class of student represents each studnet object that is unique

class Student:
	def __init__(self, ID = '00000000'):
		self.ID = ID
		self.isStaff = False

	def getID(self):
		return self.ID

