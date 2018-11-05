"""Unittest for one module

Test One
"""

import unittest
import sample


class TestOne(unittest.TestCase):
    """Unittest class for one module"""

    def test_one(self):
        """Test one"""
        self.assertTrue(sample.sample_func(False))

    def test_two(self):
        """Test two"""
        self.assertTrue(2 == 2)
