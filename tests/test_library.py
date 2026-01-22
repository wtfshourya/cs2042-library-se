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


if __name__ == "__main__":
    unittest.main()
