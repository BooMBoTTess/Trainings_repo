import unittest
import yandex_algorithm.task3_33v2 as tested_function

class MyTestCase(unittest.TestCase):
    def test_case(self):
        with open(f'tests/1.txt') as f:
            self.assertEqual(tested_function.solution(f.read().strip('\n')),
                             'YES')
        with open(f'tests/2.txt') as f:
            self.assertEqual(tested_function.solution(f.read().strip('\n')),
                             'NO')
        with open(f'tests/3.txt') as f:
            self.assertEqual(tested_function.solution(f.read().strip('\n')),
                             'YES')


if __name__ == '__main__':
    unittest.main(verbosity=2)
