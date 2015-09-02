# -*- coding: utf-8 -*-
'''
Created on 2015年9月2日

@author: edaixicuijun
'''
    # test.py  
import mock  
import unittest  
      
    # function.py  
def add_and_multiply(x, y):  
      
        addition = x + y  
        multiple = multiply(x, y)  
      
        return (addition, multiple)  
      
      
def multiply(x, y):  
      
        return x * y+3
      
class MyTestCase(unittest.TestCase):  
     
    @mock.patch('multiply')  
    def test_add_and_multiply(mock_multiply):  
      
            x = 3  
            y = 5  
      
        mock_multiply.return_value = 15  
      
        addition, multiple = add_and_multiply(x, y)  
      
        mock_multiply.assert_called_once_with(3, 5)  
      
        self.assertEqual(8, addition)  
        self.assertEqual(15, multiple)  
      
if __name__ == "__main__":  
        unittest.main()  