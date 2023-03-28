# count number of tasks user done and time needed for each task

import Student 
import csv

filename = 'studentInfo.csv'

# def task_time(int start, int end):
#     with open(filename, 'a+') as file:
#         file.write(start)

# def task_num():

with open(filename, 'a+') as file:
    writer = csv.writer(file)
    