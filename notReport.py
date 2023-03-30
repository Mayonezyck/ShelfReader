# count number of tasks user done and time needed for each task

import Student 
import csv

class notReport(Student.Student):
    
    def __init__(self, ID = '00000000', task_num = 0, currentTaskTime = -1):
        super().__init__(self, ID, task_num)
        self.filename = 'studentInfo.csv'
        self.currentTaskTime = currentTaskTime
        self.student_list = []
        self.currentRow = 0
                
    def getTaskDoneNum(self):
        return self.task_num
        
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
                           return rowreader.line_num

    def task_time(self, start, end):
         self.student_list.append(start)
         if end < 86400:
              self.student_list[-1] = end - start
    
    def taskDoneNum(self,start):
         if self.student_list[-1] == start:
                   self.student_list[1] += 0
         else:
                   self.student_list[1] += 1
                
    def renewCSV(self):
        index = 0
        with open(self.filename, 'w') as csvfile:
            rowwriter = csv.writer(csvfile)
            for row in rowwriter:
                  if index == self.currentRow:
                       rowwriter.writerow(self.student_list)
                  index += 1
