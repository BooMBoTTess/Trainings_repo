import string

uppers = string.ascii_uppercase


def to_underscore(strng) -> str:
    # your code hereDAS
    result = ''
    if type(strng) == int:
        result = str(strng)
        return result
    else:
        result = strng[0].lower()

    for l in strng[1:]:
        print(l)
        if l in uppers:
            result += '_' + l.lower()
        else:
            result += l
    return result

if __name__ == '__main__':
    print(to_underscore('TestController'))
