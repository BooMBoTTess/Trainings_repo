def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def proper_fractions(n):
    res = []
    for i in range(1,n):
        if gcd(n, i) == 1:
            res.append(gcd(n, i))
    return len(res)

if __name__ == '__main__':
    print(proper_fractions(1))
    print(proper_fractions(2))
    print(proper_fractions(15))
    assert proper_fractions(5) == 4
    assert proper_fractions(15) == 8
    assert proper_fractions(25) == 20

