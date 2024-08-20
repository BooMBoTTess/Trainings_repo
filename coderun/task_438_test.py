import task_438
import string
import random


def t_test():
    assert task_438.main('aaaza', 'aazzaa', 'azzza') == 'aazza'
    assert task_438.main('aaabbabab', 'ababaaaab', 'aabaabbab') == 'aababaab'
    assert task_438.main('xy', 'xxyy', 'yx') == 'IMPOSSIBLE'


def random_char(y):
    return ''.join(random.choice(string.ascii_lowercase) for x in range(y))

def random_test():
    for i in range(1,200):
        a,b,c = random_char(5), random_char(5), random_char(5)
        print(a,b,c)
        print(task_438.main(a,b,c))


if __name__ == '__main__':
    t_test()
    random_test()