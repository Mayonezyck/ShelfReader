#BookList starts with one book object and start building up.
#One booklist
import Book

class BookList:
    def __init__(self, book_list = None):
        self.head = None
        self.tail = None
        if book_list is not None:
            self.addMultipleBooks(book_list)
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_book
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next_book
        return count
    def addBook(self,title,barcode,callnumber):
        if self.head is None:
            self.tail = self.head = Book.Book(title,barcode,callnumber)
        else:
            self.tail.next_book = Book.Book(title,barcode,callnumber)
            self.tail = self.tail.next_book
            return self.tail
    def addMultipleBooks(self,booklist):
        for each in booklist:
            each = booklist[each]
            self.addBook(each['title'],each['barcode'],each['call number'])