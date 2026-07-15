 
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        oddsum = n *n
        evensum = n * (n + 1)
        while evensum:
            oddsum, evensum = evensum, oddsum % evensum

        return oddsum
