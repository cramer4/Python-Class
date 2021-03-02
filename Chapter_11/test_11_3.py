import unittest
from homework_11_3 import Employee

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.jj = Employee("jordan", "jamsey", 65000)

    def test_default(self):
        self.jj.raise_salary()
        self.assertEqual(self.jj.salary, 70000)

    def test_set(self):
        self.jj.raise_salary(7500)
        self.assertEqual(self.jj.salary, 72500)


if __name__ == '__main__':
    unittest.main()
