def mygcd(m, n):
    while (m != 0) and (n != 0):
        if m > n:
            m = m % n
        else:
            n = n % m
    if n == 0:
        return m
    return n

def Solution(s):
    a, b, c, d = list(map(int, s.split(' ')))
    m = b * d
    n = a * d + c * b
    i = max(m, n)
    nod = 1
    if (m % n != 0) and (n % m != 0):
        nod = mygcd(m, n)
    else:
        for i in range(i, 1, -1):
            if m % i == 0:
                nod = i
                break
    m = m//nod
    n = n//nod


    return f"{m} {n}"


if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(Solution(f.read().rstrip('\n')))