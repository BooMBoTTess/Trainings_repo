import sys

def str_to_dict(s):
    s_ans = ''
    l_l = s[0]
    letters = ''
    n = 0
    for l in s:
        if l == l_l:
            n += 1
        else:
            s_ans += l_l + str(n)
            letters += l_l
            l_l = l
            n = 1
    s_ans += l_l + str(n)
    letters += l_l


    return s_ans, letters

def main(A : str, B : str, C : str):
    A, A_l = str_to_dict(A)
    B, B_l = str_to_dict(B)
    C, C_l = str_to_dict(C)
    if not(A_l == B_l and B_l == C_l):
        return 'IMPOSSIBLE'
    ans = ''
    for i in range(0, len(A), 2):
        mean = int(round((int(A[i+1]) + int(B[i+1]) + int(C[i+1])) / 3, 0))
        ans += A[i] * mean
    return ans



if __name__ == '__main__':
    A = input()
    B = input()
    C = input()
    print(main(A, B, C))