import task_440



def t_test():
    assert task_440.main(list(map(int, '0 0 0 0'.split(' ')))) == 1
    assert task_440.main(list(map(int, '0 0 0 1'.split(' ')))) == 1
    assert task_440.main(list(map(int, '0 0 0 2'.split(' ')))) == 0
    assert task_440.main(list(map(int, '3 2 3 4'.split(' ')))) == 3
    assert task_440.main(list(map(int, '3 2 4 1'.split(' ')))) == 2
    assert task_440.main(list(map(int, '3 2 3 1'.split(' ')))) == 2
    assert task_440.main(list(map(int, '1 1 1 2'.split(' ')))) == 1
    assert task_440.main(list(map(int, '1 1 1 1'.split(' ')))) == 0
    assert task_440.main(list(map(int, '5 5 5 5'.split(' ')))) == 4
    assert task_440.main(list(map(int, '3 3 3 3'.split(' ')))) == 3
    assert task_440.main(list(map(int, '2 2 2 2'.split(' ')))) == 2
    assert task_440.main(list(map(int, '2 2 2 2'.split(' ')))) == 2
    assert task_440.main(list(map(int, '1 2 3 4'.split(' ')))) == 2
    assert task_440.main(list(map(int, '4 4 4 4'.split(' ')))) == 3


def random_test():

    for a in range(5,10):
        for b in range(5,10):
            for c in range(5,10):
                for d in range(5,10):
                    # print(a,b,c,d, '=', task_440.main([a,b,c,d]))
                    assert task_440.main([a, b, c, d]) == 4






if __name__ == '__main__':
    t_test()
    random_test()
