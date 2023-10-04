import unittest
import leetcode.task_m as main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.solution([]), [])
        self.assertEqual(main.solution([1,2,3]), [6,3,2])
        self.assertEqual(main.solution([5, 6, 1, 7]), [42, 35, 210, 30])

if __name__ == '__main__':
    unittest.main(verbosity=2)
