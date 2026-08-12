# Q16 : Library Management System (Constructor & Inheritance) 
# A library stores information about books and digital books. Create a base class Book 
# with a constructor to initialize book details. Create a derived class EBook that adds file 
# size information.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class EBook(Book):
    def filesize(self):
        self.size = 25
    def display(self):
        print("Book Title:", self.title)
        print("Book Author:",self.author)
        print("Book Size:",self.size)
e = EBook("Python", "James")
e.filesize()
e.display()