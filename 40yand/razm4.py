def Solution(students):
    prefix = [sum(students[:i]) for i in range(len(students))]
    sufix = [sum(students[i+1:]) for i in range(len(students)-1)]
    sufix.append(0)
    nedovoln = []
    nedovoln.append(sufix[0] - students[0] * (len(students)-1))
    for i in range(1, len(students)):
        nedovoln.append((students[i] * (i) - prefix[i]) + (sufix[i] - students[i] * (len(students)-1-i)))
    return nedovoln


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        index, students = f.read().rstrip('\n').split('\n')
        students = list(map(int, students.split(' ')))
        sol = Solution(students)
        print(' '.join(list(map(str, sol))))
