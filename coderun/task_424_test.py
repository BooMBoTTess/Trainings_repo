import task_424

def t_test():
    assert task_424.main(1499, 4) == '0000'
    assert task_424.main(1422, 4) == '1423'
    assert task_424.main(2500, 4) == '2507'
    assert task_424.main(250000, 6) == '250007'
    return 0

if __name__ == '__main__':
    t_test()