#checking_UI.py
from guizero import *
import readfile
filename = 'shelflist.xlsx'
shelfCheckWindow = App(title = "Shelf Checking is in Progress", width = 1000)
bookList = readfile.readfile(filename)
currentBook = None
BookTitle = None
BookCallNum = None
BookBarcode = None
BookVersion = None
ButtonBookFound = None #button number0
ButtonSubmit = None #button number1

reachlast = False
def start(student = None):
    while not reachlast:#the window should be destroyed already by the previous method
        currentBook = bookList.getHead()
        BookTitle = Text(shelfCheckWindow, text = currentBook.title,size = 30)
        BookCallNum = Text(shelfCheckWindow, text = currentBook.call_number, size = 20)
        BookVersion = Text(shelfCheckWindow, text= currentBook.version, size=20)
        ButtonBookFound = PushButton(shelfCheckWindow, text = 'Book Found', command = foundButtonPressed)
        ButtonSubmit = PushButton(shelfCheckWindow, text = 'Submit', command = submitButtonPressed)
        
        shelfCheckWindow.display()
    pass

def foundButtonPressed():
    #when the foundbutton has been pressed, the current barcode should be used to compare with the
    #list node that we are looking at, pass the currentBook.barcode to 
    
    pass

def submitButtonPressed():
    pass

def printBook():
    #BookTitle
    pass

def debug_visualizeTree(): #this method is here for debug purpose
                     #will not be included in real implementation.
    pass