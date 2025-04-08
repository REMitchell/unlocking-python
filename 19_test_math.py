import unittest
import sys
import time


class TestMath(unittest.TestCase):

    def test_5_plus_2(self):
        time.sleep(10)
        seven = 5 + 2
        self.assertEqual(seven, 7)


if __name__ == "__main__":
    unittest.main()
