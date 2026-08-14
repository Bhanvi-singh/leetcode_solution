class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        col = len(grid[0])

        gird_copy = grid

        fresh_cnt = 0
        queue = deque()

        for r in range(rows):
            for c in range(col):
                if gird_copy[r][c] == 2:
                    queue.append((r, c))
                elif gird_copy[r][c] == 1:
                    fresh_cnt += 1

        minutes = 0

        while len(queue) != 0 and fresh_cnt > 0:

            minutes += 1
            total_rotten = len(queue)

            for _ in range(total_rotten):

                i, j = queue.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                    new_i = i + dx
                    new_j = j + dy

                    if new_i < 0 or new_i == rows or new_j < 0 or new_j == col:
                        continue

                    if gird_copy[new_i][new_j] == 0 or gird_copy[new_i][new_j] == 2:
                        continue

                    fresh_cnt -= 1
                    gird_copy[new_i][new_j] = 2
                    queue.append((new_i, new_j))

        if fresh_cnt > 0:
            return -1

        return minutes