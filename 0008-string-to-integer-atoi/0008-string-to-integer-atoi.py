class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
 
        index = 0 
        while index < len(s) and s[index] == ' ':
            index += 1


        sign = 1
        if index  < len(s)  and s [index] == '-':
            sign = -1
            index += 1
        elif index < len(s) and s[index] == '+':
            index += 1
        def solve(index, num):
         
            if index >= len(s) or not s[index].isdigit():
                return num
            num = num * 10 + int(s[index])
            return solve(index + 1, num)

        num = solve(index, 0) * sign

        # 32-bit integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
 
        return num

