import sys


def main(A : str):
    L = A.split(' ')
    pairs = {}
    for word in L:
        for i in range(len(word) - 1):
            a, b = word[i], word[i+1]
            if (a + b) in pairs.keys():
                pairs[a+b] += 1
            else:
                pairs[a+b] = 1

    max_in_dict_pairs = max(pairs.values())
    ans = ''
    for key, elem in pairs.items():
        if elem == max_in_dict_pairs:
            if key > ans:
                ans = key

    return ans

if __name__ == '__main__':
    A = input()
    print(main(str(A)))