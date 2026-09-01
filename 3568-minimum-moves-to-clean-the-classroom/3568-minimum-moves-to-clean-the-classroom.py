class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start_r = start_c = 0
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1
                elif classroom[i][j] == 'S':
                    start_r, start_c = i, j

        all_mask = (1 << k) - 1

        # (row, col, energy, mask)
        q = deque()
        q.append((start_r, start_c, energy, 0))

        # For each (r,c,mask), maximum energy seen
        best = {}
        best[(start_r, start_c, 0)] = energy

        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == all_mask:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Clean litter
                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]

                    # Recharge
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    key = (nr, nc, nmask)

                    # Same position + same cleaned litter,
                    # agar pehle hi zyada energy ke saath aaye hain
                    # to current state useless hai.
                    if key in best and best[key] >= ne:
                        continue

                    best[key] = ne
                    q.append((nr, nc, ne, nmask))

            moves += 1

        return -1