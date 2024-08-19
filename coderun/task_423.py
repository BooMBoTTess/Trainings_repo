import sys

def poisk(a, x):

    next_j = len(a) - 1
    prev_j = 0
    next_a = a[next_j]
    prev_a = a[0]
    while (prev_j + 1) != next_j:
        target_j = prev_j + ((next_j - prev_j) // 2)

        if x > a[target_j]:
            prev_j = target_j
            prev_a = a[target_j]
        elif x < a[target_j]:
            next_j = target_j
            next_a = a[target_j]
        elif x == a[target_j]:
            return target_j + 1
    delta_prev = x - prev_a
    delta_next = next_a - x
    if delta_prev <= delta_next:
        return prev_j + 1
    else:
        return next_j + 1



def main(n, k, a, x):
    ans = []
    for x_i in x:
        if x_i <= a[0]:
            ans.append(1)
        elif x_i >= a[len(a) - 1]:
            ans.append(len(a))
        else:
            ans.append(poisk(a, x_i))




    print('\n'.join(list(map(str, ans))))
    return 0


if __name__ == '__main__':
    r1 = list(map(int, input().split(' ')))
    r2 = list(map(int, input().split(' ')))
    r3 = list(map(int, input().split(' ')))

    main(r1[0], r1[1], r2, r3)
