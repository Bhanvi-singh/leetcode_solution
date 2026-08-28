class Solution:
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Palindrome possible?
        if sum(x % 2 for x in cnt) > 1:
            return ""

        # Middle character
        middle = ""
        if n % 2 == 1:
            for i in range(26):
                if cnt[i] % 2 == 1:
                    middle = chr(i + ord('a'))
                    cnt[i] -= 1
                    break

        # Try to keep target's left half
        half = n // 2
        result = []

        for i in range(half):
            x = ord(target[i]) - ord('a')

            cnt[x] -= 2
            result.append(target[i])

            if cnt[x] < 0:
                break

        else:
            # Target's left half is possible
            if n % 2 == 1:
                result.append(middle)

            left = ''.join(result)
            candidate = left + left[:half][::-1]

            if candidate > target:
                return candidate

            if n % 2 == 1:
                result.pop()

        # Move backwards and make one character bigger
        while result:
            ch = result.pop()
            x = ord(ch) - ord('a')

            cnt[x] += 2

            # Find smallest character bigger than target[i]
            for y in range(x + 1, 26):

                if cnt[y] >= 2:
                    cnt[y] -= 2
                    result.append(chr(y + ord('a')))

                    # Fill remaining half with smallest characters
                    for k in range(26):
                        while cnt[k] >= 2:
                            cnt[k] -= 2
                            result.append(chr(k + ord('a')))

                    if n % 2 == 1:
                        result.append(middle)

                    left = ''.join(result)
                    candidate = left + left[:half][::-1]

                    return candidate

        return ""