def Solution(P, V, Q, M):
    result = 0
    range = P - Q
    if range < 0:
        range *= -1

    if range == 0:
        result += max(V, M) * 2 + 1
    elif range > V + M:
        result += V * 2 + 1
        result += M * 2 + 1
    elif range <= V + M:
        result += V * 2 + 1
        result += M * 2 + 1
        result -= 1 - (range - V - M)

    return result



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        P, V = map(int, f.readline().strip('\n').split(' '))
        Q, M = map(int, f.readline().strip('\n').split(' '))
        print(Solution(P, V, Q, M))