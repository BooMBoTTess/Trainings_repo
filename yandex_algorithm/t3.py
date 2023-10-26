def a():
    n = 10
    a = 10
    b = 9
    count = 0
    arr = []
    for round in range(1, n):
        for i in range(a):
            for j in range(a):
                if ((i - j) >= b) or ((j - i) >= b):
                    count += 1
        print(round, count)

n = 10
a = 10
b = 9
sp, sv = [], []
for round in range(n):
    count = 0
    for i in range(a * round):
        for j in range(a * round):
            if ((i - j) >= b) or ((j - i) >= b):
                count += 1
    print(round, count)