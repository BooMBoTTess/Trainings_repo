import sys

def main(A : int, n: int):

    AL = A // (10 ** (n // 2))
    AR = A % (10 ** (n // 2))

    while (sum(map(int,str(AL))) != sum(map(int,str(AR)))) or (len(str(AL)) > n // 2):
        AR += 1
        if len(str(AR)) > n // 2:
            AL += 1
            AR %= 10 ** (n//2)
            if len(str(AL)) > (n // 2):
                return '0'*n


    return str(AL) + '0' * (n//2-len(str(AR))) + str(AR)

def main_e(A : int, n: int):
    AL = A // (10 ** (n // 2))
    AL = sum(map(int, str(AL)))
    AR = A % (10 ** (n // 2))
    AR = sum(map(int, str(AR)))


    if sum(AL) > sum(AR):





    elif sum(map(int, str(AL))) < sum(map(int, str(AR))):
        return 0
    else:
        return str(A)


    while (sum(map(int, str(AL))) != sum(map(int, str(AR)))) or (len(str(AL)) > n // 2):
        AR += 1
        if len(str(AR)) > n // 2:
            AL += 1
            AR %= 10 ** (n // 2)
            if len(str(AL)) > (n // 2):
                return '0' * n



if __name__ == '__main__':
    A = input()
    n = len(A)
    ans = main(str(A), n)
    print(ans)