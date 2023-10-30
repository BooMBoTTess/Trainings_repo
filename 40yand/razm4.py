def Solution(students):
    k = len(students) - 2
    nk = k
    p = [sum(students[1:]) - (students[0] * (len(students) - 1))]
    index = 1
    while k != 0 and k != -1:
        p.append(p[index - 1] - (students[index] - students[index - 1]) * k)

        index += 1
        k -= 2
    if len(students) % 2 == 0:
        p.append(p[-1])
        index += 1
        k = 2
    else:
        k = 1
    while k <= nk:
        p.append(p[index - 1] + (students[index] - students[index - 1]) * k)

        index += 1
        k += 2


    return p


if __name__ == '__main__':
    print(Solution([3, 7, 8, 10, 15, 16]))
    print(Solution([3, 7, 8, 10, 15]))

    with open('input.txt', 'r') as f:
        index, students = f.read().rstrip('\n').split('\n')
        students = list(map(int, students.split(' ')))
        sol = Solution(students)
        print(' '.join(list(map(str, sol))))
