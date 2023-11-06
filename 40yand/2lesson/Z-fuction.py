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

def max_substring(hashed_s, x_arr, p):
    from1 = 1
    arr = []
    for from2 in range(2, len(strok) + 1):
        max_len = 0
        for k in range(len(strok) - from2, -1, -1):
            slen = k+1
            if is_equal(hashed_s, x_arr, p, from1, from2, slen) and slen > max_len:
                max_len = slen
        arr.append(max_len)
    arr.insert(0,0)
    return arr


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        strok = f.readline().rstrip('\n')
        x = 257
        p = 10**9 + 7
        hashed_s, x_arr = hash_s(strok, x, p)
        print(' '.join(map(str, max_substring(hashed_s, x_arr, p))))


