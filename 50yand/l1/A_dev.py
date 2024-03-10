def Solution(P, V, Q, M):
    result = 0
    if P == Q:
        return max(M, V) * 2 + 1


    if P > Q:
        tmpQ, tmpM = Q, M
        Q, M = P, V
        P, V = tmpQ, tmpM

    Left_P = P - V
    Right_P = P + V
    Left_Q = Q - M
    Right_Q = Q + M
    print(P, V, Q, M)
    print(Left_P, Right_P, Left_Q, Right_Q)
    result += Right_P - Left_P + 1
    print(result)

    if Left_Q < Left_P and Right_Q > Right_P:
        return Right_Q - Left_Q + 1

    if Left_P < Left_Q and Right_P > Right_Q:
        return Right_P - Left_P + 1

    if Right_P == Left_Q:
        result += abs(Right_Q - Left_Q)
    elif Right_P < Left_Q:
        result += abs(Right_Q - Left_Q) + 1
    elif Right_P < Q:
        result += abs(Right_Q - Right_P)
    else:
        result += abs(Right_Q - Right_P)


    return result



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        P, V = map(int, f.readline().strip('\n').split(' '))
        Q, M = map(int, f.readline().strip('\n').split(' '))
        print(Solution(P, V, Q, M))