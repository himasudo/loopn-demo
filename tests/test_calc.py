import sys
import unittest

sys.path.insert(0, "src")
import calc


class CalcTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
