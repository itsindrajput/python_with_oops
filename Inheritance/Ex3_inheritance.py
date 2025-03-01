"""
Develop a Python program that defines a class representing a book. Create an instance of the book class and initialize its attributes such as title, author, and publication year.
"""
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")

# Creating an instance of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Displaying book details
book1.display_info()
