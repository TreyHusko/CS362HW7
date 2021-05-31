import unittest
import LeapYear

class testCaseLeapYear(unittest.TestCase):
    def testLeapYear(self):
        self.assertEqual(LeapYear.LeapYear(2004), True)
    def testLeapYear2(self):
        self.assertEqual(LeapYear.LeapYear(1900), False)
    def testLeapYear3(self):
        self.assertEqual(LeapYear.LeapYear(2000), True)
if __name__ == "__main__":
    unittest.main()