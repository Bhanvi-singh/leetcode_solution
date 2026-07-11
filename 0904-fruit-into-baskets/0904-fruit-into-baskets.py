class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        mydict  = {}
        L = 0
        R = 0
        ans = 0
        n = len(fruits)
        while R < n:
            if fruits[R] in mydict:
                mydict[fruits[R]] += 1
            else:
                mydict[fruits[R]] = 1
            while len(mydict) > 2:
                mydict[fruits[L]] -= 1
                if mydict[fruits[L]] == 0:
                    del mydict[fruits[L]]
                L += 1
            ans = max(ans, R - L + 1)
            R += 1
        return ans
                


        