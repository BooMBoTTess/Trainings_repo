def mygcd(a, b):
    while b:
        a, b = b, a % b
    return a


def Solution(s):
    a, b, c, d = list(map(int, s.split(' ')))
    m = b * d
    n = a * d + c * b
    i = max(m, n)
    nod = 1
    nod = mygcd(m, n)
    m = m//nod
    n = n//nod


    return f"{m} {n}"


if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(Solution(f.read().rstrip('\n')))