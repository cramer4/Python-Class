import unittest
from homework_11_1 import get_city

class MyTestCase(unittest.TestCase):
    def test_something(self):
        country_city = get_city("paris", "france")
        self.assertEqual(country_city, "Paris, France")

if __name__ == '__main__':
    unittest.main()
