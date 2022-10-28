#this is the backend portal for the shelf chekcing process
from guizero import App, Text, TextBox, Box, PushButton
import Book
import BookList
#What is the process of shelf checking
#Get the area of interest-> Fetch a list of book from Alma
#->compile a list of books based on the inputs
#this range of books should be generated using the analysis tool from Alma, and sorted by call number
#on top of that, if the call numbers were shared among books, the version number should be sorted.


def main():
    GUInterface_login()
    #this is non-graphical user interface
    print('------------------------------')
    print('Please input the first book on the shelf')
    #Getting the input here, save as firstBook
    print('Please input the last book from the shelf')
    #getting the input here, save as LastBOok
    #compare the two call numbers:
    #COMPARE module is needed here
    #if the first book should be somewhere later in the shelf, an error should be thrown
    #to handle this error, request the user to input one book ahead/one book after
    print('Generating the list')
    #
    
 
def GUInterface_login():
    loginWindow = App(title="Log in")
    Text(loginWindow, text="Welcome!", size=40)
    Text(loginWindow, text="User ID: ",align="left")
    userNameBox = TextBox(loginWindow,text="Please enter your ID number", width=25, align="left")
    PushButton(loginWindow, text = 'clear', command = clearTextBox, args = [userNameBox], align = "left")
    PushButton(loginWindow, text = 'OK', command = GUInterface_listGenerate, args = [loginWindow], align = "bottom")
    loginWindow.set_full_screen()
    loginWindow.display()

def clearTextBox(textBox):
    textBox.clear()

def textDestroy(text):
    text.destroy()

def GUInterface_listGenerate(previousWindow):
    appDestroy(previousWindow)
    shelfCheck = App(title = "list generate")
    Text(shelfCheck, text="Where to Shelf Check", size=30)
    firstBarcode = TextBox(shelfCheck,text="Scan in the barcode of the FIRST Book",height="fill", width="fill", align="left")
    PushButton(shelfCheck, text = 'clear', command = clearTextBox, args = [firstBarcode], align = "left")
    secondBarcode = TextBox(shelfCheck,text="Scan in the barcode of the LAST Book",height="fill", width="fill", align="left")
    PushButton(shelfCheck, text = 'clear', command = clearTextBox, args = [secondBarcode], align = "left")
    PushButton(shelfCheck, text = 'OK', command = GUInterface_checkBooks, args = [shelfCheck], align = "bottom")
    shelfCheck.set_full_screen()
    shelfCheck.display()
    
def GUInterface_checkBooks(previousWindow):
    appDestroy(previousWindow)
    bookCheck = App(title = 'book Check')
    a = Book.Book('Off the record with F.D.R., 1942-1945 /','author',31840001105024,'E807 .H34')
    b = Book.Book('Franklin D. Roosevelt, an informal biography,','author',31840001101684,'E807 .H35')
    c = Book.Book('That man : an insider\'s portrait of Franklin D. Roosevelt /','author', 31840007137245,'E807 .J36 2003')
    d = Book.Book('The juggler : Franklin Roosevelt as wartime statesman /','author',31840003303312,'E807 .K48 1991')
    e = Book.Book('Commander in chief : Franklin Delano Roosevelt, his lieutenants, and their war /','author',31840002844209,'E807 .L26 1987')
    f = Book.Book('White house physician /','author',31840001105032,'E807 .M2')
    #
    BL = BookList.BookList()
    #A loop should go through every book in a list
    #for now it is just hard coding 
    BL.addBook(a)
    BL.addBook(b)
    BL.addBook(c)
    BL.addBook(d)
    BL.addBook(e)
    BL.addBook(f)
    #
    #Now that the Book list was initialized
    #Start from the first Book
    #
    #this listRunhrough method starts from the first book in the list, display required books one by one
    listRunThrough(BL)
    
    
    

def appDestroy(app):
    app.destroy()

def printBreakingLine():
    print('------------------------------')#this method simply organize the UI by inserting breaking lines of the same length

def printAnouncements(something):#similarly, this method organize the a UI by printing things with Breaking lines Surrounding 
    printBreakingLine()
    print(something)
    printBreakingLine()
    
def decisionMaking(barCode, currentNode):
    if(barCode == currentNode.value.getBarcode()):
        return 0#return True if the barcodes match thus indicating the book in place
    else:
        compareBook = currentNode.next#get the next Node to compare
        while(compareBook != None):#if it is not the end of the list
            compareBarcode = compareBook.value.getBarcode()#get the barcode of next book
            if(compareBarcode == barCode):#if they match
                print('reach')
                compareBook.value.needsAnounce()#mark the book who needs action, return false
                return 1
            compareBook = compareBook.next#move to the next book
        return -1#move to another book
    
def listRunThrough(bookList):
    inPlace = 0
    notInPlace = 0
    missing = 0
    currentNode = bookList.getFirstNode()
    currentBook = currentNode.value
    reachLast = False#this flag counts if the list reaches the last element
    while(reachLast == False):
        printBreakingLine()
        currentBook.printBook()
        printBreakingLine()
        currentBarcode = currentBook.barcode
        print('[1] In place | [2] Missing | ')
        response = int(input())
        if(response == 1):
            result = decisionMaking(currentBarcode,currentNode)
        else:
            result = decisionMaking(response, currentNode)
    
        if(result == 0):
            inPlace+=1
        elif(result == -1):
            missing+=1
        else:
            notInPlace+=1
        currentNode = currentNode.next
        if(currentNode == None):
            printAnouncements('You\'ve reached the end of the list, please wait until the report to generate')
            reachLast = True
        else:    
            currentBook = currentNode.value

    
    
    
main()