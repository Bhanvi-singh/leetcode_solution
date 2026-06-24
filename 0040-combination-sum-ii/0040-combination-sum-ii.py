class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def solve(ind, total, subset):
            
            if total == 0:
                result.append(subset[:])
                return 

            if total < 0:
                return

            
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]: 
                    continue

            #pick
        
                subset.append(candidates[i])
            
        
            #not pick
             
            
                solve(i + 1, total - candidates[i], subset)

                subset.pop()

        solve(0, target, [])
        return result
        