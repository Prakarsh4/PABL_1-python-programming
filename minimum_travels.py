class Solution:
    def minMen(self, arr):   # 👈 correct name
        n = len(arr)
        intervals = []
        
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n - 1, i + arr[i])
                intervals.append((left, right))
        
        intervals.sort()
        
        res = 0
        i = 0
        curr_end = 0
        max_reach = 0
        
        while curr_end < n:
            found = False
            
            while i < len(intervals) and intervals[i][0] <= curr_end:
                max_reach = max(max_reach, intervals[i][1] + 1)
                i += 1
                found = True
            
            if not found:
                return -1
            
            res += 1
            curr_end = max_reach
        
        return res
