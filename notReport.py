# count number of tasks user done and time needed for each task

import Student 
import csv

class notReport(Student.Student):
    
    def __init__(self, ID = '00000000', task_num = 0, currentTaskTime = -1):
        super().__init__(self, ID, task_num)
        self.filename = 'studentInfo.csv'
        self.currentTaskTime = currentTaskTime
        self.student_list = []
                
    def getTaskDoneNum(self):
        return self.task_num
        
    # find the row of this student with its id number
    def getPosition(self, id):
	    with open(self.filename, newline='') as csvfile:
                 rowreader = csv.reader(csvfile)
                 for row in rowreader:
                      if row[0] == str(id):
                           print(rowreader.line_num)
                           for element in row:
                                 self.student_list.append(element)
                                 print(self.student_list)
                           return rowreader.line_num

    def task_time(self, start, end):
         with open(self.filename, newline='') as csvfile:
              pass
    
    def taskDoneNum(self,row):
         if self.currentTaskTime == -1:
                   self.student_list[1] += 0
         else:
                   self.student_list[1] += 1
         with open(self.filename, 'w') as csvfile:
                 rowwriter = csv.writer(csvfile)
                 
