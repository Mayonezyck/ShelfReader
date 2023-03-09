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
        
    def showNextBook(self):
        self.currentBook = self.currentBook.next_book
        self.BookTitle.clear()
        self.BookTitle.append(self.currentBook.title)
        self.BookCallNum.clear()
        self.BookCallNum.append(self.currentBook.call_number)
        self.BookVersion.clear()
        self.BookVersion.append(self.currentBook.version)
        
    def foundButtonPressed(self):
        #when the foundbutton has been pressed, check if the startCounting flag is on
        #The startCounting flag should be on when within a small session, the first "not in place" book was encountered.
        if(self.startCounting):#this if and else block is used to do the shifitng of the N size block along the linked list
            pass
        else:
            self.desiredBookArray.remove(self.desiredBookArray[0])
            self.expandDesiredBookArray()#TODO: if nothing will be done in the if statement block, omit it.
        
        self.showNextBook()

        for i in self.desiredBookArray:# this is for debugging
            print(i)
        print('')
        
        pass

    def submitButtonPressed(self):
        pass
    def printBook(self):
        #BookTitle
        pass

    def reorderLoop(self): #this method initiates the reorder loop.
        #It takes in the actualBookArray and desiredBookArray, it will call the matrixgenerate.py
        #after getting the matrix back from the call, it will pass the matrix to the instruction.py
        #the instruction.py will have a solution dictionary and solution index passed back. 
        #Using the solution dictionary and solution index, the book reordering solution should be performed at this order
        #Create a temporary Book object, as "Book in the hand", its initial value should be the first book needed to be fixed on the shelf
        #The loop should be: use the "Book in the hand" as the key, find where it should fit, replace it, and the replaced book is the new
        #"Book in the hand" 
        #For the extra book in the list, it will point to "-1". We can let the student pull out all the books needed to be picked out first
        
                   
        pass