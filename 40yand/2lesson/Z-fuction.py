def hash_s(input_string, x, p):
    n = len(input_string)
    letter_a = 96
    hash = [0]
    x_len = [0] * (n+1)
    x_len[0] = 1
    x_len[1] = 1
    position = 1

    for c in input_string:
        num_c = ord(c)-letter_a
        hash.append((hash[position-1] * x + num_c) % p)
        x_len[position] = (x_len[position-1] * x) % p
        position += 1
    return hash, x_len

def is_equal(hash, x_arr, p, from1, from2, slen):
    return (
        (hash[from1 + slen - 1] + hash[from2 - 1] * x_arr[slen]) % p ==
        (hash[from2 + slen - 1] + hash[from1 - 1] * x_arr[slen]) % p
    )

def bin_find(hashed_s, x_arr, p, from1, from2):
    hashed_s.append(0)
    L = 0
    R = len(hashed_s) - from2 + 1
    X = 0
    if is_equal(hashed_s, x_arr, p, from1, from2, X) and not is_equal(hashed_s, x_arr, p, from1, from2, X + 1):
        return 0

    while L < R:
        X = (R + L) // 2
        if is_equal(hashed_s, x_arr, p, from1, from2, X) and not is_equal(hashed_s, x_arr, p, from1, from2, X + 1):
            return X
        elif is_equal(hashed_s, x_arr, p, from1, from2, X):
            L = X
        else:
            R = X

    return X


def max_substring(hashed_s, x_arr, p):
    from1 = 1
    arr = []
    for from2 in range(2, len(strok) + 1):
        arr.append(bin_find(hashed_s, x_arr, p, from1, from2))
    arr.insert(0,0)
    return arr


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        strok = f.readline().rstrip('\n')
        x = 33
        p = 10**9 + 7
        hashed_s, x_arr = hash_s(strok, x, p)
        print(' '.join(map(str, max_substring(hashed_s, x_arr, p))))


