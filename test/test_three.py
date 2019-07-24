"""Unittest for one module

Third test
"""

import unittest
import sample


class ThirdTest(unittest.TestCase):
    """Unittest class for sample module"""

    def test_one(self):
        """Test one"""
        self.assertTrue(sample.sample_func(False))

    def test_two(self):
        """Test two"""
        self.assertTrue(3 == 3)


if __name__ == "__main__":
    unittest.main()
