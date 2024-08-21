import sys

def main(players : list):
    queens = 4
    ans = 0
    players.sort()
    for i in range(len(players)):
        queens -= players[i]
        if queens < 0:
            return 4 - ans
        elif queens == 0:
            ans += 1
            return 4 - ans
        else:
            ans += 1
    if queens - 2 > 0:
        return 1
    else:
        return 4 - ans


if __name__ == '__main__':
    A = list(map(int, input().split(' ')))
    print(main(A))
