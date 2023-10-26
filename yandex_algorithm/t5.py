def Solution(s):
    index = s.split('\n')
    n = int(index[0])
    arr = list(map(int, index[1].split(' ')))
    Lshell, Rshell = [0],[max(arr)]
    for book in arr:
        if (book - Lshell[len(Lshell)-1]) <= (Rshell[0] - book):
            if book >= Lshell[len(Lshell)-1]:
                Lshell.append(book)
        else:
            if book <= Rshell[0]:
                Rshell.insert(0, book)

    Lshell.extend(Rshell)
    return len(Lshell[1:-1])


if __name__ == '__main__':
    f = open('input.txt', 'r')
    print(Solution(f.read().rstrip('\n')))