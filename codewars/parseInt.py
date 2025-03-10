import re
simple_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7 ,
                  'eight': 8, 'eigh': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
                  'fifth': 5, 'thir': 3, 'ni': 9, 'for': 4, 'fif': 5, 'sev': 7,
                  'twen': 2
                  }


def simple_word(s: str) -> int:
    return simple_numbers[s]

def teen_word(s: str) -> int:
    s = s.rstrip('teen')
    return simple_word(s) + 10

def decimals_word(s: str) -> int:
    s = s.rstrip('ty')
    return simple_word(s) * 10


def parse_int(string):
    words = re.split('[\s-]', string)
    print(words)
    score = 0
    for word in words:
        if word.find('teen') != -1:
            score += teen_word(word)
        elif word.find('ty') != -1:
            score += decimals_word(word)
        elif word == 'hundred':
            left, right = divmod(score, 1000)
            score = (left*10 + right) * 100
            print(left, right)
        elif word == 'thousand':
            score *= 1000
        elif word == 'million':
            score *= 1000000
        elif word in simple_numbers:
            score += simple_word(word)
        print(score)
    return score



if __name__ == '__main__':
    print(parse_int('one'))
    print(parse_int('eleven'))
    print(parse_int('fourteen'))
    print(parse_int('fifthteen'))
    print(parse_int('twenty four'))
    print(parse_int('two hundred thirty and four'))
    print(parse_int('two hundred thirty-four'))
    print(parse_int('nine'))
    print(parse_int('nineteen'))
    print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))
    print(parse_int('two hundred and one'))
    print(parse_int('twenty thousand and one'))
    print(parse_int('twenty thousand two hundred and one'))