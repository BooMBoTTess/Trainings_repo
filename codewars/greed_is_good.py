TRIPLET_MAP = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
COUNTED_MAP = {1: 100, 5: 50}


def score(dice):
    map = {d: 0 for d in dice}
    score = 0

    for d in dice:
        map[d] += 1
    for key, value in map.items():
        if value == 3:
            score += TRIPLET_MAP[key]
        elif value < 3:
            if key in COUNTED_MAP:
                score += COUNTED_MAP[key] * value
        else:
            score += TRIPLET_MAP[key]
            if key in COUNTED_MAP:
                value -= 3
                score += COUNTED_MAP[key] * value
    return score

if __name__ == '__main__':
    print(score([1,5,3]))