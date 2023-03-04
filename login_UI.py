#login_UI.py

from guizero import *
import csv
import Student
# import task_UI

filename = 'studentInfo.csv'
loginWindow = App(title="Log in")

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

# make the user interface
def login():
	Text(loginWindow, text="\nWelcome!\n", size=40)
	Text(loginWindow, text="ID number: ",align="left")
	UserIdBox = TextBox(loginWindow, text="Please enter your ID number", width=25, align="left")
	UserIdBox.text_color = 'grey'
	UserIdBox.when_clicked = toEnter   # clear text in textbox when click on it
	arrange_box=Box(loginWindow, height="fill")
	PushButton(arrange_box, text = 'OK', command = check, args = [UserIdBox], align = "right")	
	nextPage = PushButton(loginWindow, text = 'Next', align = "bottom")
	# nextPage.when_clicked = nextWindow
	# loginWindow.set_full_screen()
	loginWindow.display()

	def toEnter():
   		UserIdBox.value = '';UserIdBox.text_color='black'
	
def check(idbox):
		id = idbox.value
		if len(id) == 7:
			# print(len(id))
			checkExist(id)	
		else:
			loginWindow.error('!!!', 'ID number must be 7 digit!')	

# def nextWindow():
# 	loginWindow.hide()
# 	task_UI.task()