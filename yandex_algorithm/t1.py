def Solution(s):
    symbols = []
    for i in range(len(s)):
        if (s[i] == '+') or (s[i] == '-'):
            symbols.append(s[i])

    s = s.replace('+', ';')
    s = s.replace('-',';')
    s = list(map(int, s.split(';')))
    ans = s[0]
    for i in range(1, len(s)):
        if symbols[i - 1] == '+':
            ans += s[i]
        else:
            ans -= s[i]


    return ans

if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(Solution(f.read().rstrip('\n')))