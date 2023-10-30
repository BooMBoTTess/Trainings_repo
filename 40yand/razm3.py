def Solution(s1, s2):
    dict_s1 = {}
    dict_s2 = {}
    for i in s1:
        if i in dict_s1.keys():
            dict_s1[i] += 1
        else:
            dict_s1[i] = 1
    for i in s2:
        if i in dict_s2.keys():
            dict_s2[i] += 1
        else:
            dict_s2[i] = 1
    if dict_s1.keys() != dict_s2.keys():
        return False
    for i in dict_s1.keys():
        if dict_s1[i] != dict_s2[i]:
            return False

    return True


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        s1, s2 = f.read().rstrip('\n').split('\n')
        if Solution(s1,s2):
            print("YES")
        else:
            print("NO")