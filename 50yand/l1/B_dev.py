def Solution(match_prev, match, home):
    total_score = (match_prev[0] + match[0], match_prev[1] + match[1])
    need = total_score[1] - total_score[0]
    if home == 1:
        #Первая дома им нужно больше голов сейчас
        if match_prev[0] == match_prev[1]:
            return need + 1
        else:
            return need
    else:
        return need + 1




if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        prev = tuple(map(int, f.readline().strip('\n').split(':')))
        cur = tuple(map(int, f.readline().strip('\n').split(':')))
        H = int(f.readline().strip('\n'))
        print(Solution(prev, cur, H))