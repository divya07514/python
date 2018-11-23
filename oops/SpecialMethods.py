class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# Overriding special methods on order to give own implementation.
    def __str__(self):
        return f"{self.title} by {self.author}"


b = Book('Python Rocks', "Divya", 240)
print(b)
