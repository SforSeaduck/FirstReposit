from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author_or_director, year):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    @abstractmethod
    def description(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, year, number_of_pages):
        super().__init__(title, author, year)
        self.number_of_pages = number_of_pages

    def description(self):
        return f"Title: {self.title}, Author: {self.author_or_director}, Year: {self.year}, Pages: {self.number_of_pages}"

class Magazine(LibraryItem):
    def __init__(self, title, author_or_director, year, issue_number):
        super().__init__(title, author_or_director, year)
        self.issue_number = issue_number

    def description(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}, Issue Number: {self.issue_number}"

class DVD(LibraryItem):
    def __init__(self, title, director, year, duration):
        super().__init__(title, director, year)
        self.duration = duration

    def description(self):
        return f"Title: {self.title}, Director: {self.author_or_director}, Year: {self.year}, Duration: {self.duration} minutes"

if __name__ == "__main__":
    book = Book("1922", "Stephen King", 2010, 368)
    magazine = Magazine("National Geographic", "Various", 2023, 12)
    dvd = DVD("Interstellar", "Christopher Nolan", 2014, 169)

    print(book.description())
    print(magazine.description())
    print(dvd.description())
