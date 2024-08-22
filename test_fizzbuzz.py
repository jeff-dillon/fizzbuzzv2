import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        """Test If the number is evenly divisble by 3, the function returns 'fizz'"""
        self.assertEqual(fizzbuzz(3), "fizz")
    
    def test_buzz(self):
        """Test If the number is evenly divisble by 5, the function returns 'buzz'"""
        self.assertEqual(fizzbuzz(5), "buzz")
    
    def test_fizzbuzz(self):
        """Test If the number is evenly divisble by 3 and 5, the function returns 'fizzbuzz'"""
        self.assertEqual(fizzbuzz(15), "fizzbuzz")


if __name__ == "__main__":
    unittest.main(verbosity=2)