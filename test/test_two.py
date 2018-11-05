"""Unittest for one module

Another test
"""

import unittest
import sample


class AnotherTest(unittest.TestCase):
    """Unittest class for one module"""

    def test_one(self):
        """Test one"""
        self.assertTrue(sample.sample_func(False))

    def test_two(self):
        """Test two"""
        self.assertTrue(3 == 3)
