import unittest
from main import addieren, subtraktion, multiplizieren

        
class test_taschenrechner(unittest.TestCase):
    def test_multiplikation(self):
        self.assertEqual(multiplizieren(10, 2), 5)
        self.assertEqual(multiplizieren(15, 2), 7.5)
        self.assertEqual(multiplizieren(50, 0), "ERROR: Division durch 0 ist nicht erlaubt")

    def test_addition(self):
        self.assertEqual(addieren(2, 3), 5)
        self.assertEqual(addieren(-1, 1), 0)
        self.assertEqual(addieren(0, 0), 0)

    def test_subtraktion(self):
        self.assertEqual(subtraktion(3, 3), 0)
        self.assertEqual(subtraktion(-1, 1), -2)
        self.assertEqual(subtraktion(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
