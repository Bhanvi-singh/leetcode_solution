class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        """
        :type x: int
        :rtype: bool
        """
        def func(s, left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return func(s, left + 1, right - 1)
        return func(s, 0, len(s) - 1)