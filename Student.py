# this class of student represents each studnet object that is unique

class Student:
	def __init__(self, ID = '00000000', task_num = 0):
		self.ID = ID
		self.isStaff = False
		self.task_num = task_num

	def __str__(self):
		return str(self.ID)
	
	def getID(self):
		return self.ID
	
	def getTaskDoneNum(self):
		return self.task_num

