#login_UI.py

from guizero import *
import csv
import Student

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

def toEnter():
    UserIdBox.value = ''
    UserIdBox.text_color='black'

def check(id):
	if len(id) == 7:
		print(len(id))
		checkExist(id)	
	else:
		loginWindow.error('!!!', 'ID number must be 7 digit!')	

Text(loginWindow, text="\nWelcome!\n", size=40)
Text(loginWindow, text="ID number: ",align="left")
UserIdBox = TextBox(loginWindow, text="Please enter your ID number", width=25, align="left")
UserIdBox.text_color = 'grey'
UserIdBox.when_clicked = toEnter   # clear text in textbox when click on it
id_number = str(UserIdBox.value)  
# value is "Please enter your ID number", use UserIdBox.append(string) to update
arrange_box=Box(loginWindow, height="fill")
PushButton(arrange_box, text = 'OK', command = check, args = [id_number], align = "right")
# PushButton(loginWindow, text = 'Next', command = GUInterface_listGenerate, args = [loginWindow], align = "bottom")
# loginWindow.set_full_screen()
loginWindow.display()


