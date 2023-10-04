import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.Solution(5), '3\n1 2 4 5')
        self.assertEqual(main.Solution(10), '3\n1 3 9 10')
        self.assertEqual(main.Solution(1), '0\n1')
        self.assertEqual(main.Solution(100), '1\n1')
        self.assertEqual(main.Solution(1000), '1\n1')

if __name__ == '__main__':
    unittest.main(verbosity=2)
