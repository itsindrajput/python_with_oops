class Book:
    def __init__(self,name,pages):
        self.name = name
        self.pages = pages

    def __gt__(self,other):
        return self.pages > other.pages

    def __lt__(self,other):
        return self.pages < other.pages

book1 = Book("Merchant",100)
book2 = Book("venice",200)

print(book1 > book2 )
print(book1 < book2 )