class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

       
        dp = [0] * (k + 1)
        dp[0] = 1

        
        open_seg = [0] * (k + 1)

        for _ in range(n - 1):
            for j in range(k, 0, -1):
                
                open_seg[j] = (
                    open_seg[j] + dp[j - 1]
                ) % MOD

                 
                dp[j] = (
                    dp[j] + open_seg[j]
                ) % MOD

        return dp[k]