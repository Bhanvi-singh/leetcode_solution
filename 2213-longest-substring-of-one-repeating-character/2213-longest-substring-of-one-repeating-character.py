class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # [leftChar, rightChar, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def merge(left, right):
            leftChar = left[0]
            rightChar = right[1]

            prefix = left[2]
            suffix = right[3]
            best = max(left[4], right[4])

            # If boundary characters are same
            if left[1] == right[0]:

                # Join suffix of left + prefix of right
                best = max(best, left[3] + right[2])

                # If complete left segment has same character
                if left[2] == left[5]:
                    prefix = left[5] + right[2]

                # If complete right segment has same character
                if right[3] == right[5]:
                    suffix = left[3] + right[5]

            length = left[5] + right[5]

            return [
                leftChar,
                rightChar,
                prefix,
                suffix,
                best,
                length
            ]

        def build(node, start, end):
            if start == end:
                ch = s[start]
                tree[node] = [ch, ch, 1, 1, 1, 1]
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, start, end, index, ch):
            if start == end:
                tree[node] = [ch, ch, 1, 1, 1, 1]
                return

            mid = (start + end) // 2

            if index <= mid:
                update(
                    node * 2,
                    start,
                    mid,
                    index,
                    ch
                )
            else:
                update(
                    node * 2 + 1,
                    mid + 1,
                    end,
                    index,
                    ch
                )

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryIndices)):
            index = queryIndices[i]
            ch = queryCharacters[i]

            update(1, 0, n - 1, index, ch)

            ans.append(tree[1][4])

        return ans