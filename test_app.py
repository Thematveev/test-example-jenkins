import unittest


def summa(a, b):
    return a + b



class TestSumFunc(unittest.TestCase):
    def test_basic_operation(self):
        r = summa(1, 2)
        self.assertEqual(3, r)
