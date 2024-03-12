def Solution(match_prev, match, home):
    total_score = (match_prev[0] + match[0], match_prev[1] + match[1])
    need = total_score[1] - total_score[0]
    print(need)
    if need < 0:
        return 0
    if need == 0:
        if home == 2:
            if match_prev[0] <= match[1]:
                return 1
            else:
                return 0
        else:
            if match_prev[1] >= match[0]:
                return 1
            else:
                return 0

    if home == 2:
        #2я игра дома
        if match_prev[0] >= match[1]:
            return need
        else:
            return need + 1
    else:
        if match_prev[1] >= match[0] + need:
            return need + 1
        return need






if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        prev = tuple(map(int, f.readline().strip('\n').split(':')))
        cur = tuple(map(int, f.readline().strip('\n').split(':')))
        H = int(f.readline().strip('\n'))
        print(Solution(prev, cur, H))