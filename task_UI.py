# confirm the date and the booklist waiting for check

from guizero import *
from datetime import *
import os
# import readfile
import login_UI

# get today's date in textual month, day and year	
today = date.today().strftime("%B %d, %Y") 

path = 'shelflist.xlsx'

# get file modified date
timestamp = os.path.getmtime(path)
datestamp = datetime.fromtimestamp(timestamp)

# bookList = readfile.readfile(path)
# book = bookList.getHead()

def task():
    taskWindow = App(title="Confirm your task")
    confirm_date = TitleBox(taskWindow, "Today is")
    Text(confirm_date, text=today, size=14)
    confirm_fileDate = TitleBox(taskWindow, "The file is uploaded on")
    Text(confirm_fileDate, text=datestamp, size=14)
    confirm_firstBook = TitleBox(taskWindow, "The first book in this list is")
    # Text(confirm_firstBook, text=book.call_number, size=14)
    # Text(confirm_firstBook, text=book.title, size=12)
    # taskWindow.set_full_screen()
    taskWindow.display()
