import unittest
from file_to_test import my_dict, add_to_dict
import os



class Testing(unittest.TestCase):
        
        def test_my_dict(self):
            test_dict = my_dict
            self.assertEqual(len(test_dict),0)

        def test_add_dict(self):
            test_dict = add_to_dict(my_dict)
            self.assertEqual(len(test_dict),0)

unittest.main()
