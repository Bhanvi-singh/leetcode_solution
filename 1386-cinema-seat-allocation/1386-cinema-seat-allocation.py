class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        rows = {}

        for r, c in reservedSeats:
            if r not in rows:
                rows[r] = set()
            rows[r].add(c)

        # Rows with no reserved seats -> 2 families each
        ans = (n - len(rows)) * 2

        for seats in rows.values():

            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            if not (seats & left) and not (seats & right):
                # Both left and right groups are available
                ans += 2

            elif not (seats & left) or not (seats & middle) or not (seats & right):
                # At least one group is available
                ans += 1

        return ans