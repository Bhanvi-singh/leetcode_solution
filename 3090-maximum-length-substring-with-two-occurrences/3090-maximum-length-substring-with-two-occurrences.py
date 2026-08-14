class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {}
        l = 0
        r = 0
        maxi = 0
        n = len(s)
        for r in range(n):
            my_dict[s[r]] = my_dict.get(s[r], 0) + 1
            while my_dict[s[r]] > 2:
                my_dict [s[l]] -= 1
                l +=1
            length = r - l + 1
            
            maxi= max(maxi,length)
        return maxi