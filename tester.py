import unittest
import leetcode.task_m_45 as tested_function

class MyTestCase(unittest.TestCase):
    def test_case(self):
        s = tested_function.Solution()
        self.assertEqual(s.jump([2,3,1,1,4]), 2)
        self.assertEqual(s.jump([2, 3, 0, 1, 4]), 2)
        self.assertEqual(s.jump([1 for i in range(1000)]), 999)
        self.assertEqual(s.jump([1000 for i in range(1000)]), 1)



if __name__ == '__main__':
    unittest.main(verbosity=2)

#[2,3,1,1,4] -> 2