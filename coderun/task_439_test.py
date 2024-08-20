import task_439

def t_test():
    assert task_439.main('ABCABC A') == 'BC'
    assert task_439.main('AA A A A A ') == 'BC'


if __name__ == '__main__':
    t_test()