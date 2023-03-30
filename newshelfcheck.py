#This program is the newer version of shelfcheck.py
#This will be an under-construction version. 
#from guizero import *
import Book,BookList
import login_UI
import checking_UI
import task_UI
import time
import notReport

student = login_UI.login_UI()
student.login()
currentStudent = student.getStudent()
print(currentStudent, type(currentStudent))

taskUI = task_UI.task_UI()
taskUI.task()

startTime = time.perf_counter()

cui = checking_UI.checking_UI()
cui.start(currentStudent)

endTime = time.perf_counter()
print('Start Time:',startTime)
print('End Time', endTime)

