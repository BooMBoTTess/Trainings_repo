def dbl_linear(n):
    z = 1
    for i in range(n):
        z = (i+1) * i + 1
        print(z)
    return z

if __name__ == '__main__':
    print(dbl_linear(10))