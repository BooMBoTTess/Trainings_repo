def Solution(num):

    darr = [[0, 0, 1, 1], [0, 0, 1, 1]]
    for i in range(4, num + 1):
        s3 = darr[0][i // 3] + 1
        s2 = darr[0][i // 2] + 1
        s1 = darr[0][i - 1] + 1
        if (s3 <= s2 <= s1) and (i % 3 == 0):
            darr[0].append(s3)
            darr[1].append(i // 3)
        elif (s2 <= s1) and (i % 2 == 0):
            darr[0].append(s2)
            darr[1].append(i // 2)
        else:
            darr[0].append(s1)
            darr[1].append(i - 1)

    tmp = num
    path = [tmp]
    while tmp != 0:
        path.append(darr[1][tmp])
        tmp = darr[1][tmp]
    path.reverse()
    return f'{darr[0][num]}\n{" ".join(map(str, path[1:]))}'


if __name__ == "__main__":
    print(Solution(int(input())))
