import unittest
from mypackage import functions


class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calc1 = functions.sum(8, 2)
        self.assertEqual(calc1, 10, 'The sum is wrong.')

        calc2 = functions.sub(8, 2)
        self.assertEqual(calc2, 6, 'The sub is wrong.')

        calc3 = functions.mult(8, 2)
        self.assertEqual(calc3, 16, 'The mult is wrong.')

        calc4 = functions.div(8, 2)
        self.assertEqual(calc4, 4, 'The div is wrong.')


if __name__ == '__main__':
    unittest.main()
