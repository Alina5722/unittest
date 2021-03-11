import unittest
import main
class tests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(main.sum(10,-5),5)

    def test_diff(self):
        self.assertEqual(main.diff(129,29),100)

    def test_function(self):
        self.assertTrue(main.function(4,4),True)

    def test_fact(self):
        self.assertEqual(main.fact(5), 120)

    def test_simple(self):
        self.assertEqual(main.simple(10), {3,5,7})

if __name__ =='__main__':
    unittest.main()