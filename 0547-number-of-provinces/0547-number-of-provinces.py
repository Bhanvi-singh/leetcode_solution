class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n  = len(isConnected)
        visited = [False] * n
        count = 0
        
        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                queue = [i]
                while queue:
                    city = queue.pop(0)
                    for j in range(n):
                        if isConnected[city][j]==1 and not visited[j]:
                            visited[j]= True
                            queue.append(j)
        return count
