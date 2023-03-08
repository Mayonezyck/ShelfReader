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
        self.barcodeBox = None
        self.reachlast = False
        self.startCounting = False
        self.theNthBookTracer = self.bookList.getHead()
        self.N = 20#this is heuristic value of N
        self.desiredBookArray = []
        self.expandDesiredBookArray(self.N)
        self.actualBookArray = []
    def expandDesiredBookArray(self, count = 1):
        for i in range(count):
            self.desiredBookArray.append(self.theNthBookTracer)
            self.theNthBookTracer = self.theNthBookTracer.next_book
    def start(self, student = None):
        def toEnter():
            self.barcodeBox.value = ''
            self.barcodeBox.text_color='black'
        print(student)
        while not self.reachlast:#the window should be destroyed already by the previous method
            self.currentBook = self.bookList.getHead()
            self.BookTitle = Text(self.shelfCheckWindow, text = self.currentBook.title,size = 30)
            self.BookCallNum = Text(self.shelfCheckWindow, text = self.currentBook.call_number, size = 20)
            self.BookVersion = Text(self.shelfCheckWindow, text= self.currentBook.version, size=20)
            self.barcodeBox = TextBox(self.shelfCheckWindow, text="scan in barcode if not found", width=25, align="top")
            self.barcodeBox.text_color = "grey"
            self.barcodeBox.when_clicked = toEnter
            self.ButtonBookFound = PushButton(self.shelfCheckWindow, text = 'Book Found', command = self.foundButtonPressed)
            self.ButtonSubmit = PushButton(self.shelfCheckWindow, text = 'Submit', command = self.submitButtonPressed)
            self.shelfCheckWindow.display()
        pass
    def showNextBook(self):
        self.currentBook = self.currentBook.next_book
        self.BookTitle.clear()
        self.BookTitle.append(self.currentBook.title)
        self.BookCallNum.clear()
        self.BookCallNum.append(self.currentBook.call_number)
        self.BookVersion.clear()
        self.BookVersion.append(self.currentBook.version)
    def foundButtonPressed(self):
        if(self.startCounting):
            pass
        else:
            self.desiredBookArray.remove(self.desiredBookArray[0])
            self.expandDesiredBookArray()
        self.showNextBook()
        for i in self.desiredBookArray:
            print(i)
        print('')
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