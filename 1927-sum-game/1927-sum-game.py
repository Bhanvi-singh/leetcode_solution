class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # If total number of ? is odd,
        # Alice can always make the sums unequal.
        if (left_q + right_q) % 2 == 1:
            return True

        # Difference between known sums
        diff = left_sum - right_sum

        # Difference in number of ? on both sides
        q_diff = left_q - right_q

        # Bob can make the sums equal only in this case
        return diff * 2 != -9 * q_diff