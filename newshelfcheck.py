#This program is the newer version of shelfcheck.py
#This will be an under-construction version. 
#from guizero import *
import Book,BookList
import login_UI
import checking_UI
import task_UI

student = login_UI.login_UI()
student.login()
currentStudent = student.getStudent()

taskUI = task_UI.task_UI()
taskUI.task()

cui = checking_UI.checking_UI()
cui.start(currentStudent)
