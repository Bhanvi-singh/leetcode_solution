class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        # dp[i] = maximum number of valid non-overlapping
        # palindromes using s[0:i]
        dp = [0] * (n + 1)

        for i in range(n):
            # Don't use s[i]
            dp[i + 1] = max(dp[i + 1], dp[i])

            # Odd length palindrome
            left = i
            right = i

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    dp[right + 1] = max(
                        dp[right + 1],
                        dp[left] + 1
                    )
                    break

                left -= 1
                right += 1

            # Even length palindrome
            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    dp[right + 1] = max(
                        dp[right + 1],
                        dp[left] + 1
                    )
                    break

                left -= 1
                right += 1

        return dp[n]