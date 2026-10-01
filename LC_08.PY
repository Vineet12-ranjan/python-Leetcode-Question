class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Leading spaces ignore karo
        while i < n and s[i] == ' ':
            i += 1

        # 2. Sign check karo
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Number convert karo
        num = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            i += 1

        num = num * sign

        # 4. 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num

