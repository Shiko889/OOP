import pytest
from lib.book import Book

class TestBook(object):
    def test_book_initialization(self):
        book = Book("Introduction to Python", "John Doe", 200)
        assert book.title == "Introduction to Python"
        assert book.author == "John Doe"
        assert book.pages == 200
        assert book.current_page == 1

    def test_turn_page(self):
        book = Book("Introduction to Python", "John Doe", 200)
        book.turn_page()
        assert book.current_page == 2
        book.turn_page()
        assert book.current_page == 3
