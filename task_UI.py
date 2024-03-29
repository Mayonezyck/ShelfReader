# confirm the date and the booklist waiting for check

from guizero import *
import time
import os
import readfile
#import login_UI

class task_UI:

    def __init__(self) -> None:
        self.today = time.ctime(time.time())
        self.path = 'shelflist.xlsx'
        self.taskWindow = App(title="Confirm your task", width = 480, height = 320)
        self.datestamp = time.ctime(os.path.getmtime(self.path)) # get file modified date
        self.bookList, temp = readfile.readfile(self.path)
        self.book = self.bookList.getHead()
   

    def task(self):
        Text(self.taskWindow, text="", size=10)
        Text(self.taskWindow, text="Current Task", size=30)
        Text(self.taskWindow, text="", size=5)
        confirm_date = TitleBox(self.taskWindow, "Today is", height=90, width=750)
        Text(confirm_date, text=self.today, size=14)
        confirm_fileDate = TitleBox(self.taskWindow, "The file is uploaded on", height=90, width=750)
        Text(confirm_fileDate, text=self.datestamp, size=15)
        confirm_firstBook = TitleBox(self.taskWindow, "The first book in this list is", height=105, width=750)
        Text(confirm_firstBook, text=self.book.call_number, size=15)
        Text(confirm_firstBook, text=self.book.title, size=15)
        Text(self.taskWindow, text="", size=5)
        #button for confirm
        yes = PushButton(self.taskWindow, text='Yes', command=self.killWindow, align='left', height="fill", width="fill")
        yes.text_size = 18
        #button for abort
        no = PushButton(self.taskWindow, text='No', command=self.findHelp, align="right", height="fill", width="fill")
        no.text_size = 18
        self.taskWindow.set_full_screen()
        self.taskWindow.display()
    
    def killWindow(self):
        self.taskWindow.destroy() 
    
    def findHelp(self):
        self.taskWindow.warn("Stop", "Go back and talk to your supervisor!")  
        
