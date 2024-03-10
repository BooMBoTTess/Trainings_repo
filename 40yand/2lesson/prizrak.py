def hash_s(input_string, x, p):
    n = len(input_string)
    hash = [0]
    hash_reverse = [0]
    x_len = [0] * (n+1)
    x_len[0] = 1
    x_len[1] = 1

    position = 1
    letter_a = 48
    for c in input_string:
        num_c = ord(c) - letter_a
        hash.append((hash[position-1] * x + num_c) % p)
        x_len[position] = (x_len[position-1] * x) % p
        position += 1

    position = 1
    for c in input_string[::-1]:
        num_c = ord(c) - letter_a
        hash_reverse.append((hash_reverse[position - 1] * x + num_c) % p)
        position += 1

    return hash, hash_reverse, x_len


def is_equal(hash, x_arr, p, from1, from2, slen):
    return (
        (hash[from1 + slen - 1] + hash[from2 - 1] * x_arr[slen]) % p ==
        (hash[from2 + slen - 1] + hash[from1 - 1] * x_arr[slen]) % p
    )


def Solution(hashed_s, hashed_s_rev, x_arr, p):
    for Z in range(len(hashed_s), len(hashed_s)//2 - 1, -1):
        for P in range(Z, Z//2, -1):
            hashed_target = hashed_s * x_arr[p] + hashed_s_rev[]



if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        strok = f.readline().rstrip('\n')
        x = 100
        p = 10**20 + 7
        hashed_s, hash_s_rev, x_arr = hash_s(strok, x, p)
        print(hashed_s, hash_s_rev)


