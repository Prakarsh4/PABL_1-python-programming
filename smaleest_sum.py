class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        left = 0
        curr_sum = 0
        min_len = float('inf')
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum >= x:
                min_len = min(min_len, right - left + 1)
                curr_sum -= arr[left]
                left += 1
        
        return 0 if min_len == float('inf') else min_len
