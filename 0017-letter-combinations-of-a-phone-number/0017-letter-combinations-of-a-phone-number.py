class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        char_Map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        def solve(ind, subset):
            if ind >= len(digits):
                result.append("".join(subset))
                return
            for ch in char_Map[digits[ind]]:
              subset.append(ch)
              solve(ind + 1, subset)
              subset.pop()
        solve(0, [])
        return result