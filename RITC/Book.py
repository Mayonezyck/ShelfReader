#this class of book represents one single book object that is unique and have a barcode of its
#own

#
class Book:
    title = ''
    author = ''
    barcode = -1
    call_number = ''
    inPlace = False
    hasNote = False
    
    def __init__(self, title, author, barcode, call_number):
        self.title = title
        self.author = author
        self.barcode = barcode
        self.call_number = call_number
        self.inPlace = False
        
    def getBarcode(self):
        return self.barcode
    
    def printBook(self):
        if(self.hasNote):
            print('!!!!!!!!!!!!!!')
            print('Action Needed')
        print('[Title]: \n\t' + self.title)
        print('[Author]: \n\t' + self.author)
        print('[Call number]: \n\t' + self.call_number)
        
    def founD(self):
        self.inPlace = True
        
    def needsAnounce(self):
        self.hasNote = True