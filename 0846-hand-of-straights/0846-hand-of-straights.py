class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        freq = Counter(hand)
        for num in hand:
            if freq[num] == 0:
                continue
            for curr in range(num, num + groupSize):
                if freq[curr] == 0:
                    return False
                freq[curr] -= 1
        return True