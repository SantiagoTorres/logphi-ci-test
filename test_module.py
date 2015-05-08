#!/usr/bin/env python
"""
    test_module

    Test suite for the module

"""
import unittest
import module
import os

class test_module(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass



    def test_get_filenames(self):

        # verify that a list is returned
        self.assertTrue(isinstance(module.get_filenames(), list))

        # verify that the list is long enough
        filenames = module.get_filenames()
        self.assertTrue(len(filenames) > 0)

        # verify that the returned list is only files
        for filename in filenames:
            self.assertFalse(os.path.isdir(filename))

    def test_check_sums(self):

        # verify
        filenames = module.get_filenames()
#        self.assertTrue(isinstance(module.check_sums(filenames), list))





if __name__ == '__main__':
    unittest.main()

