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
        self.taskWindow = App(title="Confirm your task")
        self.datestamp = time.ctime(os.path.getmtime(self.path)) # get file modified date
        self.bookList = readfile.readfile(self.path)
        self.book = self.bookList.getHead()
   

    def task(self):
        confirm_date = TitleBox(self.taskWindow, "Today is", height="fill", width="fill")
        confirm_date.font
        Text(confirm_date, text=self.today, size=14)
        confirm_fileDate = TitleBox(self.taskWindow, "The file is uploaded on", height="fill", width="fill")
        Text(confirm_fileDate, text=self.datestamp, size=14)
        confirm_firstBook = TitleBox(self.taskWindow, "The first book in this list is", height="fill", width="fill")
        Text(confirm_firstBook, text=self.book.call_number, size=14)
        Text(confirm_firstBook, text=self.book.title, size=14)
        #self.taskWindow.set_full_screen()
        #TODO:button for confirm
        #TODO:button for abort
        self.taskWindow.display()
    

