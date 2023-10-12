import unittest
#import yandex_algorithm.task3_30 as main
import leetcode.task_l_21 as main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        f = open('test.txt', 'r')
        self.assertEqual(main.Solution(f.read().rstrip('\n')), '4\n1 2 3 4')

if __name__ == '__main__':
    unittest.main(verbosity=2)
