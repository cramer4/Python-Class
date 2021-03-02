import unittest
from homework_11_2 import get_city

class MyTestCase(unittest.TestCase):
    def test_something(self):
        country_city = get_city("paris", "france")
        self.assertEqual(country_city, "Paris, France")
    def test_something_2(self):
        country_city = get_city("paris", "france", "2100000")
        self.assertEqual(country_city, "Paris, France\nPopulation: 2100000")

if __name__ == '__main__':
    unittest.main()
