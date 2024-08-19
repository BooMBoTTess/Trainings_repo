import sys


def main():
    A = int(input())
    B = int(input())
    N = int(input())

    Bn = B // N
    if B % N != 0:
        Bn += 1

    if Bn >= A:
        print('No')
    else:
        print('Yes')

    print(A, B, Bn)

if __name__ == '__main__':
    main()