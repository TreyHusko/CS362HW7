import FizzBuzz
import unittest

class testCaseFizzBuzz(unittest.TestCase):
    def test_FizzBuzz(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3), "Fizz")

if __name__ == "__main__":
    unittest.main()