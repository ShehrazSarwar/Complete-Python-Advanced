# Dunder Methods also known as Magic Methods
# Called Operator Overloading In other programming languages like C++

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # Some others are
    # __ne__(self, other):
    # __le__(self, other):
    # __ge__(self, other):

    def __add__(self, other):
        return self.num_pages + other.num_pages

    # Some others are
    # __sub__(self, other):
    # __mul__(self, other):
    # __rmul__(self, other):   Only when left side of argument is integer and other is object
    # __mod__(self, other):
    # __truediv__(self, other):
    # __floordiv__(self, other):

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "author":
            return self.author
        elif key == "title":
            return self.title
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"The key {key} was not found"


book1 = Book("Atomic Habbits", "James Clear",273)
book2 = Book("Grokking Algorithms", "Aditya Bhargava",280)
book3 = Book("The Psychology of Money", "Morgan Housel",320)

print(book1)
# print(book2)
# print(book3)

print(book1 == book2)
print(book1 < book3)
print(book2 > book3)

print(book2 + book3)

print("Atomic" in book1)
print("Morgan" in book2)
print("Morgan" in book3)

print(book1["author"])
print(book2["title"])
print(book3["audio"])

