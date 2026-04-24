class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        
        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # if number exceeds target → break
                if candidates[i] > target:
                    break
                
                # include current number
                path.append(candidates[i])
                
                # move to next index (i+1 → use once only)
                backtrack(i + 1, path, target - candidates[i])
                
                # backtrack
                path.pop()
        
        backtrack(0, [], target)
        return res
