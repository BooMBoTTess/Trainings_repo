import sys

def main(A : int, n: int):
    AL = A // (10 ** (n // 2))
    AR = A % (10 ** (n // 2))

    while (sum(map(int,str(AL))) != sum(map(int,str(AR)))) or ():
        AR += 1
        if len(str(AR)) > n // 2:
            AL += 1

    return str(AL) + '0' * (n//2-len(str(AR))) + str(AR)


if __name__ == '__main__':
    A = input()
    n = len(A)
    ans = main(int(A), n)
    print(ans)