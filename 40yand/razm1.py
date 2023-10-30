def sol(tmp):
    minimum = min(tmp)
    for el in range(len(tmp)):
        if tmp[el] != minimum:
            return tmp[el]
    return 'NOT FOUND'
def Solution(s):
    s = s.split('\n')
    input_str = list(map(int, s[1].split(' ')))
    arr = s[2:]
    tmp = []
    for elem in arr:
        elem = list(map(int, elem.split(' ')))
        tmp = input_str[elem[0] : elem[1]+1]

        ans = -1
        print(sol(tmp))


if __name__ == '__main__':
    f = open('input.txt', 'r')
    Solution(f.read().rstrip('\n'))