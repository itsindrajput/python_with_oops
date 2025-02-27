class Book:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages
 
book1 = Book(100)
book2 = Book(200)
book3 = Book(300)
print("Total No. of Books = ", book1 + book2 + book3)