import unittest
from src.library import Library


class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        self.library.add_book("B001", "Clean Code", "Robert Martin")
        self.assertIn("B001", self.library.books)

    def test_add_duplicate_book_raises_error(self):
        self.library.add_book("B001", "Clean Code", "Robert Martin")
        with self.assertRaises(ValueError):
            self.library.add_book("B001", "Another Book", "Another Author")

class TestLibrarySprint2(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("B002", "Refactoring", "Martin Fowler")

    def test_borrow_available_book(self):
        self.library.borrow_book("B002")
        self.assertEqual(
            self.library.books["B002"]["status"],
            "Borrowed"
        )

    def test_borrow_unavailable_book_raises_error(self):
        self.library.borrow_book("B002")
        with self.assertRaises(ValueError):
            self.library.borrow_book("B002")

    def test_return_book_updates_status(self):
        self.library.borrow_book("B002")
        self.library.return_book("B002")
        self.assertEqual(
            self.library.books["B002"]["status"],
            "Available"
        )



if __name__ == "__main__":
    unittest.main()
