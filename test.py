#test file
import Book, BookList,readfile

filename = 'shelflist.xlsx'
booklist = readfile.readfile(filename)
print(booklist.head.next_book)
print(booklist.tail.next_book)
print(booklist)