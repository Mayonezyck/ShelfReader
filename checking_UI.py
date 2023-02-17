#checking_UI.py
from guizero import *
import readfile
filename = 'shelflist.xlsx'
shelfCheckWindow = App(title = "Shelf Checking is Starting")
bookList = readfile.readfile(filename)
currentBook = None
BookTitle = None
BookCallNum = None
BookBarcode = None
BookVersion = None
def start(student = None):
    #the window should be destroyed already by the previous method
    currentBook = bookList.getHead()
    BookTitle = Text(shelfCheckWindow, text = currentBook.title,size = 30)
    BookCallNum = Text(shelfCheckWindow, text = currentBook.call_number, size = 20)
    shelfCheckWindow.display()
    pass

def printBook():
    #BookTitle
    pass