class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '':
            return 0
        numbers = list('0123456789')
        result = 0
        pos = 0
        length = len(s) - 1
        sign = True

        # whitespaces
        while pos <= length and s[pos] == ' ':
            pos += 1
            print(pos)
        if pos == length+1:
            return 0

        #Sign
        if s[pos] == '-':
            sign = False
            pos += 1
        elif s[pos] == '+':
            sign = True
            pos += 1

        # numbers
        while (pos <= length) and (s[pos] in numbers) :
            result = result * 10 + int(s[pos])
            print(result)
            pos += 1



        if sign:
            if result < 2147483647:
                return result
            else:
                return 2147483647
        else:
            print(result)
            if result * -1 > -2147483648:
                return result * -1
            else:
                return -2147483648

if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi('   42') == 42
    assert s.myAtoi('42') == 42
    assert s.myAtoi('-042') == -42
    assert s.myAtoi('1337c0d3') == 1337
    assert s.myAtoi('ords and 987') == 0
    assert s.myAtoi('-2147483650') == -2147483648
    assert s.myAtoi('2147483649') == 2147483647
    assert s.myAtoi('    ') == 0
    assert s.myAtoi('   3') == 3