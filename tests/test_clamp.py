import sys
import unittest

sys.path.insert(0, "src")
import clamp as clamp_mod


class ClampTests(unittest.TestCase):
    def test_inside(self):
        self.assertEqual(clamp_mod.clamp(5, 0, 10), 5)
        self.assertEqual(clamp_mod.clamp(-7, -10, -2), -7)
        self.assertEqual(clamp_mod.clamp(2.5, 2, 3), 2.5)

    def test_below(self):
        self.assertEqual(clamp_mod.clamp(-1, 0, 10), 0)
        self.assertEqual(clamp_mod.clamp(-100, -5, 5), -5)
        self.assertEqual(clamp_mod.clamp(1.5, 2, 3), 2)

    def test_above(self):
        self.assertEqual(clamp_mod.clamp(11, 0, 10), 10)
        self.assertEqual(clamp_mod.clamp(50, -5, 7), 7)
        self.assertEqual(clamp_mod.clamp(-1, -9, -3), -3)

    def test_boundaries(self):
        self.assertEqual(clamp_mod.clamp(0, 0, 10), 0)
        self.assertEqual(clamp_mod.clamp(10, 0, 10), 10)

    def test_degenerate(self):
        self.assertEqual(clamp_mod.clamp(3, 3, 3), 3)
        self.assertEqual(clamp_mod.clamp(9, 4, 4), 4)
        self.assertEqual(clamp_mod.clamp(-9, 4, 4), 4)

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            clamp_mod.clamp(1, 5, 0)
        with self.assertRaises(ValueError):
            clamp_mod.clamp(3, 4, 3)
        with self.assertRaises(ValueError):
            clamp_mod.clamp(100, 1, -1)


if __name__ == "__main__":
    unittest.main()
