from django.test import TestCase
from ebooks.models import myBooks
from django.core.exceptions import ValidationError
# Create your tests here.
class myBooksTestCase(TestCase):
    def setUp(self):
        self.book=myBooks(title='Python', author='gp',genre='progs', price=56, stock=10)
    def test_in_stock(self):
        self.book.in_stock=5
        self.assertTrue(self.book.in_stock)
        self.book.price=10
        self.assertTrue(self.book.in_stock)
        self.book.in_stock=0
        self.assertFalse(self.book.in_stock)
        self.book.price =-0
        self.assertFalse(self.book.price)
        book1 = myBooks(price=10.00, stock=5)
        self.assertEqual(book1.get_total_price(), 9000.00)

        '''Test with price=20.00 and stock=2'''
        book2 = myBooks(price=20.00, stock=2)
        self.assertEqual(book2.get_total_price(), 40.00)
    def test_clean_negative_price(self):
        '''Create an instance of MyBook with a negative price'''
        book = myBooks(price=-10.00, stock=5)

        # Check if clean raises a ValidationError for negative price
        with self.assertRaises(ValidationError):
            book.clean()  # Call the clean method to validate

    def test_clean_negative_stock(self):
        # Create an instance of MyBook with a negative stock
        book = myBooks(price=10.00, stock=-5)

        # Check if clean raises a ValidationError for negative stock
        with self.assertRaises(ValidationError):
            book.clean()  # Call the clean method to validate

    def test_clean_valid_price_and_stock(self):
        # Create an instance of MyBook with valid price and stock
        book = myBooks(price=10.00, stock=5)

        # Ensure that clean doesn't raise any exception (valid values)
        try:
            book.clean()  # Call the clean method to validate
        except ValidationError:
            self.fail("clean() raised ValidationError unexpectedly!")









