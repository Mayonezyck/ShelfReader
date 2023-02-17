#login_UI.py

from guizero import *
import csv
import Student

class login_UI:
	
	def addStaff(id):
		pass

	def checkExist(id):
		with open("studentInfo.csv", 'r') as file:
			csvreader = csv.reader(file)
			for row in csvreader:
				print(row)
				if id == row:
					return Student.student(id)
				else:
					addStaff(id)
		return None

	


login_UI.checkExist(1)
print(1)
# return 
