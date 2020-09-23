import unittest
import funcs

class TestCases(unittest.TestCase):
    def test_f_1(self):
    	self.assertEqual(funcs.f(1), 9)
    def test_f_1a(self):
    	self.assertEqual(funcs.f(-100), 69800)

    def test_f_2(self):
    	self.assertEqual(funcs.g(1, 2), 5)
    def test_f_2a(self):
    	self.assertEqual(funcs.g(-100, 23), 10529)  

    def test_f_3(self):
      self.assertEqual(funcs.hypotenuse(4, 3), 5)
    def test_f_3a(self):
      self.assertEqual(funcs.hypotenuse(-4, -3), 5)

    def test_f_4(self):
      self.assertTrue(funcs.is_positive(12532))
      self.assertFalse(funcs.is_positive(-12532))
# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

