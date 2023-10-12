import unittest
import yandex_algorithm.task3_33v2 as tested_function

class MyTestCase(unittest.TestCase):
    def test_something(self):
        f = open('09.txt', 'r')
        self.assertEqual(tested_function.solution(f.read().strip('\n')),
                         'YES')

if __name__ == '__main__':
    unittest.main(verbosity=2)
