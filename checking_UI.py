#checking_UI.py
from guizero import *
import readfile

class checking_UI:
    def __init__(self):
        self.filename = 'shelflist.xlsx'
        self.shelfCheckWindow = App(title = "Shelf Checking is in Progress", width = 1000)
        self.bookList = readfile.readfile(self.filename)
        self.currentBook = None
        self.BookTitle = None
        self.BookCallNum = None
        self.BookBarcode = None
        self.BookVersion = None
        self.ButtonBookFound = None #button number0
        self.ButtonSubmit = None #button number1

        self.reachlast = False
    def start(self, student = None):
        print(student)
        while not self.reachlast:#the window should be destroyed already by the previous method
            currentBook = self.bookList.getHead()
            BookTitle = Text(self.shelfCheckWindow, text = currentBook.title,size = 30)
            BookCallNum = Text(self.shelfCheckWindow, text = currentBook.call_number, size = 20)
            BookVersion = Text(self.shelfCheckWindow, text= currentBook.version, size=20)
            ButtonBookFound = PushButton(self.shelfCheckWindow, text = 'Book Found', command = self.foundButtonPressed)
            ButtonSubmit = PushButton(self.shelfCheckWindow, text = 'Submit', command = self.submitButtonPressed)
            
            self.shelfCheckWindow.display()
        pass

    def foundButtonPressed(self):
        #when the foundbutton has been pressed, the current barcode should be used to compare with the
        #list node that we are looking at, pass the currentBook.barcode to 
        
        pass

    def submitButtonPressed(self):
        pass

    def printBook(self):
        #BookTitle
        pass

    def debug_visualizeTree(self): #this method is here for debug purpose
                        #will not be included in real implementation.
        pass