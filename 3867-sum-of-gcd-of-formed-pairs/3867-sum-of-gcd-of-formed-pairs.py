 
class Solution(object):

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        n = len(nums)

        prefixGcd = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(self.gcd(x, mx))

        prefixGcd.sort()

        ans = 0
        i = 0
        j = n - 1

        while i < j:
            ans += self.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans