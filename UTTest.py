import unittest

class UTTest(unittest.TestCase):

    def start_test(self):
        test_value = True
        print("Test value is not true.")
        self.assertTrue(test_value, print)

    def test_value(self):
        first_value = "Employee"
        second_value = "Employee"
        print("Values are equal")
        self.assertEqual(first_value, second_value, print)