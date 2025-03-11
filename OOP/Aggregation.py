# Aggregation = Independant relationship

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_books(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("Fast Pwr Library...")

book1 = Book("Atomic Habbits","James Clear")
book2 = Book("The Psychology of Money","Morgan Housel")
book3 = Book("Grokking Algorithms","Aditya Bhargava")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

print(library.name)
for book in library.list_books():
    print(book)