import unittest
import leetcode.task_e_1512 as tested_function

class MyTestCase(unittest.TestCase):
    def test_case(self):
        s = tested_function.Solution()
        self.assertEqual(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]), 4)
        self.assertEqual(s.numIdenticalPairs([1, 1, 1, 1]), 6)
        self.assertEqual(s.numIdenticalPairs([1, 2, 3]), 0)
        self.assertEqual(s.numIdenticalPairs([1]), 0)
        self.assertEqual(s.numIdenticalPairs([1 for i in range(100)]), 495)



if __name__ == '__main__':
    unittest.main(verbosity=2)
