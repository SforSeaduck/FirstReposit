import pytest
from library import Book, Library

@pytest.fixture(scope="class")
def library():
    return Library()

@pytest.fixture(scope="class")
def sample_books():
    return [
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell")
    ]

class TestLibrary:
    def test_add_book(self, library, sample_books):
        book = sample_books[0]
        library.add_book(book)
        assert len(library.books) == 1
        assert library.books[0] == book

    def test_remove_book(self, library, sample_books):
        for book in sample_books:
            library.add_book(book)
        
        removed_book = library.remove_book("1984")
        assert removed_book.title == "1984"
        assert len(library.books) == 2
        assert all(b.title != "1984" for b in library.books)

    def test_remove_nonexistent_book(self, library):
        with pytest.raises(ValueError) as excinfo:
            library.remove_book("Nonexistent Book")
        assert str(excinfo.value) == "No book found with title 'Nonexistent Book'."

    def test_add_non_book(self, library):
        with pytest.raises(TypeError) as excinfo:
            library.add_book("Not a Book")
        assert str(excinfo.value) == "Only instances of Book can be added."

    def test_repr(self, library, sample_books):
        for book in sample_books:
            library.add_book(book)
        assert repr(library) == f"Library(books={sample_books})"
