# from unit_testing07.simplecalc import SimpleCalc
# import unittest
#
# #  Define a class that inherits from TestCase
#
# class CalcTests(unittest.TestCase):  # notice green arrow for running test in PyCharm
#
#     calc = SimpleCalc()
#
#     def setUp(self):
#         self.calc = SimpleCalc()
#         print("Setting Up")
#         #  this setup will run before every test
#
#     def tearDown(self):
#         pass
#
#     def test_add(self):
#         actual = self.calc.add(2, 4)
#         expected = 6
#         self.assertEqual(actual, expected)
#
#     def test_subtract(self):
#         actual = self.calc.subtract(6, 4)
#         expected = 2
#         self.assertEqual(actual, expected)
#
#     # def test_multiply(self):
#     #     actual = self.calc.multiply(2, 4)
#     #     expected = 8
#     #     self.assertEqual(actual, expected)
#
#     def test_multiply(self):
#         actual = self.calc.multiply(0.4, -80.9)
#         expected = -32.36
#         self.assertAlmostEqual(actual, expected)
#
#     #  self.assertEqual(actual, expected) will be wrong because:
#     #   -32.36 != -32.36000000000001
#     # Expected :-32.36000000000001
#     # Actual   :-32.36
#     # So we change to assertAlmostEqual.
#
#     def test_divide(self):
#         actual = self.calc.divide(4, 2)
#         expected = 2
#         self.assertEqual(actual, expected)
#


