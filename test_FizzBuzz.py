import FizzBuzz
import unittest

class testCaseFizzBuzz(unittest.TestCase):
    def test_FizzBuzz(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3), "Fizz")
    def test_FizzBuzz2(self):
        self.assertEqual(FizzBuzz.FizzBuzz(5), "Buzz")
    def test_FizzBuzz3(self):
        self.assertEqual(FizzBuzz.FizzBuzz(15), "FizzBuzz")
    def test_FizzBuzz4(self):
        self.assertEqual(FizzBuzz.FizzBuzz(7), 7)

if __name__ == "__main__":
    unittest.main()