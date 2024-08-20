import sys

def str_to_dict(s):
    s_ans = []
    l_l = s[0]
    letters = ''
    n = 0
    for l in s:
        if l == l_l:
            n += 1
        else:
            s_ans.append(n)
            letters += l_l
            l_l = l
            n = 1
    s_ans.append(n)
    letters += l_l


    return s_ans, letters

def count_letter(A,B,C) -> int:
    arr = [A,B,C]
    arr.sort()
    return arr[1]

def main(A : str, B : str, C : str):
    NA, LA = str_to_dict(A)
    NB, LB = str_to_dict(B)
    NC, LC = str_to_dict(C)
    if not(LA == LB and LB == LC):
        return 'IMPOSSIBLE'
    ans = ''
    for i in range(0, len(LA)):
        ans += LA[i] * count_letter(NA[i], NB[i], NC[i])
    return ans



if __name__ == '__main__':
    A = input()
    B = input()
    C = input()
    print(main(A, B, C))
