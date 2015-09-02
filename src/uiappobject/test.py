#-*-coding:utf-8-*- 
import unittest
from function import add_and_multiply
import  function

class MyTestCase(unittest.TestCase):
    def test_add_and_multiply(self):

        x = 3
        y = 5

        addition, multiple = add_and_multiply(x, y)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

if __name__ == "__main__":
    unittest.main()