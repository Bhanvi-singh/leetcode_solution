class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        cnt = Counter(s)

        half = {}
        mid = ""

        for ch in cnt:
            half[ch] = cnt[ch] // 2
            if cnt[ch] % 2:
                mid = ch

        chars = sorted(half.keys())

        m = sum(half.values())

        # Current number of distinct left-half permutations
        ways = factorial(m)
        for v in half.values():
            ways //= factorial(v)

        if ways < k:
            return ""

        ans = []

        while m:
            for ch in chars:
                if half[ch] == 0:
                    continue

                # Number of permutations if we place ch here
                nxt = ways * half[ch] // m

                if nxt >= k:
                    ans.append(ch)
                    ways = nxt
                    half[ch] -= 1
                    m -= 1
                    break
                else:
                    k -= nxt

        left = "".join(ans)
        return left + mid + left[::-1]