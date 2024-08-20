import task_438
import string
import random

custom_letters='ab'

def t_test():
    assert task_438.main('aaaza', 'aazzaa', 'azzza') == 'aazza'
    assert task_438.main('aaabbabab', 'ababaaaab', 'aabaabbab') == 'aababab'
    assert task_438.main('aaa', 'a', 'a') == 'a'
    assert task_438.main('aba', 'aba', 'aba') == 'aba'
    assert task_438.main('xy', 'xxyy', 'yx') == 'IMPOSSIBLE'
    assert task_438.main('aabbbbabbabaaaaabbababbaabaababbabbbbaabbbbabbaaaaabaabbaababbbababababbaaabbaaababbbaaabbbbaaaaaaaa', 'ababaabbbababaaaabaaabaaabaabaabbbaababbbbabbbaaabaaaabbababababbbbbaaaaaaaaabaaaabbbbbabbbbbabbaaba','abbbaaaaaaaaaaaaaabbaabbbbaaababababaabaabbaaababbabaabbabababaaaaabaabaaabaaabaabbbabbbaabaaaabaaaa')


def random_char(y):
    return ''.join(random.choice(custom_letters) for x in range(y))

def random_test():
    for i in range(1,2000):
        a,b,c = random_char(100), random_char(100), random_char(100)
        result = task_438.main(a,b,c)
        if result != 'IMPOSSIBLE':
            print(a,b,c)
            print(task_438.main(a,b,c))
            print('------------')


if __name__ == '__main__':
    t_test()
    random_test()