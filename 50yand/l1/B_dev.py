def Solution(match_prev, match, home):
    total_score = (match_prev[0] + match[0], match_prev[1] + match[1])
    need = total_score[1] - total_score[0]
    print(need)
    if home == 2:
        return need + 1
    else:
        if match_prev[1] >= need:
            return need + 1
        return need






if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        prev = tuple(map(int, f.readline().strip('\n').split(':')))
        cur = tuple(map(int, f.readline().strip('\n').split(':')))
        H = int(f.readline().strip('\n'))
        print(Solution(prev, cur, H))