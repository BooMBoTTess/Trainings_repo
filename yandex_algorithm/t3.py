# n = 100
# a = 10
# b = 1
# count = 0
# arr = []
#
# for i in range(1, a+1):
#     for j in range(1, a+1):
#         if ((i - j) >= b) or ((j - i) >= b):
#             count += 1
#
# Em = 1 * (count/100)
# for round in range(2, n):
#     Em += round * ((100-count) / 100 ** (round-1)) * (count/100)
# print(Em)



n = 10
a = 10
b = 3
sp, sv = [], []
arr = [0]
for round in range(1, n):
    count = 0
    for i in range(1, a * round + 1):
        for j in range(1, a * round + 1):
            if ((i - j) >= b) or ((j - i) >= b):
                print(i,j)
                count += 1
    arr.append(count / (a * round * a * round))

Em = arr[1]
print(1, Em, arr[1])
for x in range(2, n):
    prev_fail = 1
    for prev in range(1, x):
        prev_fail *= (1 - arr[prev])
    Em += x * arr[x] * prev_fail
    print(x, Em, arr[x], prev_fail)
print(Em)