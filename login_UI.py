#login_UI.py

from guizero import *
import csv
import Student


def login_UI(student):
	
	def addStaff(id):
		with open('studentInfo.csv', 'a+') as file:
			file.write("\n" + str(id))
			print('added')
			
	def checkExist(id):
		with open('studentInfo.csv', 'r') as file:
			isExist = False
			csvreader = csv.reader(file)
			for row in csvreader:
				# print(row[0])
				# print(str(id))
				if str(id) == row[0]:	
					isExist = True
			if isExist == False:
				addStaff(id)
		return Student.Student(id)

	checkExist(student)


login_UI(34453225)
#print('over')
# return 
