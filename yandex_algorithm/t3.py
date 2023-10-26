n = 100
a = 10
b = 50
count = 0
arr = []

for i in range(a):
    for j in range(a):
        if ((i - j) >= b) or ((j - i) >= b):
            count += 1

Em = 1 * (count/100)
for round in range(2, n):
    Em += round * ((100-count) / 100 ** (round-1)) * (count/100)
    print(Em)