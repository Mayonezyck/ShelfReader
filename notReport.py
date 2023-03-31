# count number of tasks user done and time needed for each task

import Student 
import csv
import pandas as pd

class notReport(Student.Student):
    
    def __init__(self,ID = '0000000'):
        self.ID = ID
        self.filename = 'studentInfo.csv'
        self.student_list = []
        self.currentRow = 0
        self.taskNum = 0
        
    # find the row of this student with its id number
    def getPosition(self, id):
	    with open(self.filename, newline='') as csvfile:
                 rowreader = csv.reader(csvfile)
                 for row in rowreader:
                      if row[0] == str(id):
                           self.currentRow = rowreader.line_num
                           # print(self.currentRow)
                           for element in row:
                                 self.student_list.append(element)
                                 # print(self.student_list)
                           return self.currentRow

    def task_time(self, start, end):
         if self.student_list[1] == '':
               self.taskNum = 0
         else: 
               self.taskNum = int(self.student_list[1])
         print(self.taskNum+2)
         self.student_list[self.taskNum+2] = start
         # print(self.student_list)
         print(self.student_list[self.taskNum+2])
         if end < 43200: # 12 hours
              self.student_list[self.taskNum+2] = str(float(end - start))
         print(self.student_list)
    
    def updateTaskDoneNum(self,start):
         time = float(self.student_list[self.taskNum+1])
         if self.student_list[1] == '':
               taskDone_num = 0
         else: 
               taskDone_num = int(self.student_list[1])
         if time == start:
                   taskDone_num += 0
         else:
                   taskDone_num += 1
         self.student_list[1] = str(taskDone_num)
                
    def renewCSV(self):
        studentinfo = pd.read_csv(self.filename, encoding = 'utf-8')
        # print(self.currentRow-2, self.taskNum+2)
        # print(self.student_list)
        x,y = self.currentRow-2, self.taskNum+2
        studentinfo.iloc[x,1] = self.student_list[1]
        studentinfo.iloc[x,y] = self.student_list[y]
        print('fii')
        studentinfo.to_csv(self.filename,index=False)
        print(studentinfo)

# report = notReport()
# report.getPosition('1234567')
# report.task_time(1, 40)
# report.updateTaskDoneNum(1)
# report.renewCSV()