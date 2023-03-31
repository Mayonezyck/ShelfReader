# count number of tasks user done and time needed for each task

import Student 
import csv

class notReport(Student.Student):
    
    def __init__(self):
        self.ID = '0000000'
        self.filename = 'studentInfo.csv'
        self.student_list = []
        self.currentRow = 0
        
    # find the row of this student with its id number
    def getPosition(self, id):
	    with open(self.filename, newline='') as csvfile:
                 rowreader = csv.reader(csvfile)
                 for row in rowreader:
                      if row[0] == str(id):
                           self.currentRow = rowreader.line_num
                           print(self.currentRow)
                           for element in row:
                                 self.student_list.append(element)
                                 print(self.student_list)
                           return self.currentRow

    def task_time(self, start, end):
         self.student_list.append(start)
         if end < 43200: # 12 hours
              self.student_list[-1] = end - start
         print(self.student_list)
    
    def taskDoneNum(self,start):
         time = float(self.student_list[-1])
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
        with open(self.filename, 'a+', newline='') as csvfile:
            rowwriter = csv.writer(csvfile)
            rowreader = csv.reader(csvfile)
            for index in range(len(list(rowreader))):
                  print(self.student_list)
                  if index == self.currentRow:
                       rowwriter.writerow(self.student_list)
                       print(self.student_list)

report = notReport()
report.getPosition(str(1234567))
report.task_time(1, 40)
report.taskDoneNum(1)
report.renewCSV()