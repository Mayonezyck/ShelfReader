#login_UI.py

from guizero import *
import csv
import Student
# import task_UI
class login_UI:
    def __init__(self) -> None:
        self.filename = 'studentInfo.csv'
        self.loginWindow = App(title="Log in")
        self.currentStudent = None

    def addStaff(self,id):
        with open(self.filename, 'a+') as file:
            file.write("\n" + str(id))
            print('added')
            
    def checkExist(self,id):
        with open(self.filename, 'r') as file:
            isExist = False
            csvreader = csv.reader(file)
            for row in csvreader:
                # print(row[0])
                # print(str(id))
                if str(id) == row[0]:   
                    isExist = True
            if isExist == False:
                self.addStaff(id)
        return Student.Student(id)
	
# make the user interface
    def login(self):
        def toEnter():
            UserIdBox.value = ''
            UserIdBox.text_color='black'

        Text(self.loginWindow, text="\nWelcome!\n", size=40)
        Text(self.loginWindow, text="ID number: ",align="left")
        UserIdBox = TextBox(self.loginWindow, text="Please enter your ID number", width=25, align="left")
        UserIdBox.text_color = 'grey'
        UserIdBox.when_clicked = toEnter   # clear text in textbox when click on it
        arrange_box=Box(self.loginWindow, height="fill")
        #PushButton(arrange_box, text = 'OK', command = self.check, args = [UserIdBox], align = "right")  
        PushButton(arrange_box, text = 'OK', command = self.check, args = [UserIdBox], align = "right")  
        #nextPage = PushButton(self.loginWindow, text = 'Next', align = "bottom")
        # nextPage.when_clicked = nextWindow
        # loginWindow.set_full_screen()
        self.loginWindow.display()  
             
    def getStudent(self):
        return self.currentStudent
	
    def killWindow(self):
        self.loginWindow.destroy()  

    def strToInt(self,id):
        try:
            int(id)
        except(ValueError):
            self.loginWindow.error('!!!', 'ID number cannot contain any letters or special symbols or spaces!')

    def check(self,idbox):
        id = idbox.value
        self.strToInt(id)
        if len(id) == 7 and 0 <= int(id) < 10000000:
            # print(len(id))
            self.currentStudent = self.checkExist(id)  
            self.killWindow()     
        else:    
            self.loginWindow.error('!!!', 'ID number must be 7 in length!')
