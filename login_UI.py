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


def GUI_login():
	loginWindow = App(title="Log in")
    Text(loginWindow, text="\nWelcome!\n", size=40)
    Text(loginWindow, text="User ID: ",align="left")
    userIdBox = TextBox(loginWindow,text="Please enter your ID number", width=25, align="left")
    PushButton(loginWindow, text = 'clear', command = clearTextBox, args = [userNameBox], align = "left")
    PushButton(loginWindow, text = 'OK', align = "bottom")
    # PushButton(loginWindow, text = 'OK', command = GUInterface_listGenerate, args = [loginWindow], align = "bottom")
    login_UI(userIdBox)
    # loginWindow.set_full_screen()
    loginWindow.display()