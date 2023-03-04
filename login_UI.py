#login_UI.py

from guizero import *
import csv
import Student

filename = 'studentInfo.csv'
loginWindow = App(title="Log in")
# instruct = Text(loginWindow, text="Please enter your ID number")
Id_number = ' '

def addStaff(id):
	with open(filename, 'a+') as file:
		file.write("\n" + str(id))
		print('added')
			
def checkExist(id):
	with open(filename, 'r') as file:
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
		
def login_UI(student):
	Text(loginWindow, text="\nWelcome!\n", size=40)
	Text(loginWindow, text="User ID: ",align="left")
	UserIdBox = TextBox(loginWindow,text="Please enter your ID number", width=25, align="left")
	PushButton(loginWindow, text = 'clear', command = clearTextBox, args = [UserIdBox], align = "left")
	
	Id_number = str(UserIdBox.value)
	if len(Id_number) != 7:
		loginWindow.error('!!!', 'ID number must be 7 digit!')
	else:
		login_UI(Id_number)
	print(Id_number)
    
	PushButton(loginWindow, text = 'OK', align = "bottom") 
    # PushButton(loginWindow, text = 'OK', command = GUInterface_listGenerate, args = [loginWindow], align = "bottom")
    # loginWindow.set_full_screen()
	loginWindow.display()

def clearTextBox(textBox):
    textBox.clear()