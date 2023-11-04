def hash_s(x, p, input_string):
    letter_a = 1071
    hash = [0]
    position = 1
    for c in input_string:
        num_c = ord(c)-letter_a
        hash.append((hash[position-1] * x + num_c) % p)
        position+= 1
    print(hash)
    return hash[-1]

def is_equal(hash_str1, hash_str2):
    return hash_str1 == hash_str2

def is_pohoshi(hash_str1, has_str2, pohosgest):
    p = has_str2 - hash_str1
    if p < 0:
        p *= -1
    return p < pohosgest

if __name__ == '__main__':

    f = open('input.txt','r')
    arr = f.read().rstrip('\n').split('\n')
    x = 256
    p = 10000000000 + 7
    poghosgest = []
    for s1 in arr:
        for s2 in arr:
            if s1 != s2:
                hs1 = hash_s(x, p, s1)
                hs2 = hash_s(x, p, s2)
                print(s1, s2)
                print(hs1, hs2)
                x = hs1 - hs2
                if x < 0:
                    x *= -1
                poghosgest.append(x)
                print(hs1 - hs2)
                print('**************')
    print(sorted(poghosgest))