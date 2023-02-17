#login_UI.py

from guizero import *
import csv
import Student

class login_UI:

	path = 'studentInfo.csv'
	
	def addStaff(id):
		f_write=open(path, 'w')
		csvwriter = csv.writer(f_write)
		csvwriter.writerow(id) 
		f_write.close()


		print('here')#

	def checkExist(id):
		# with open(path, 'r+') as file:
		# 	csvreader = csv.reader(file)
		# 	for row in csvreader:
		# 		print(row)
		# 		if id == row:
		# 			return Student.student(id)
		# 		else:
		# 			login_UI.addStaff(id)
		f_read=open(path, 'r')
		csvreader = csv.reader(file)
		for row in csvreader:
			print(row)
			if id == row:
				return Student.student(id)
			else:
				login_UI.addStaff(id)
				return Student.student(id)
		f_read.close()


login_UI.checkExist(1)
print(1)
# return 
