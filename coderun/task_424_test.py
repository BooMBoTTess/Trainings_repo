import task_424

def t_test():
    assert task_424.main(1499, 4) == '1506'
    assert task_424.main(1414, 4) == '1414'
    assert task_424.main(9998, 4) == '9999'
    assert task_424.main(9900, 4) == '9999'
    assert task_424.main(, 4) == '0101'
    assert task_424.main(9913, 4) == '9999'
    assert task_424.main(1422, 4) == '1423'
    assert task_424.main(2500, 4) == '2507'
    assert task_424.main(250000, 6) == '250007'
    assert task_424.main(6609, 4) == '6639'
    assert task_424.main(1356, 4) == '1405'
    return 0

if __name__ == '__main__':
    t_test()