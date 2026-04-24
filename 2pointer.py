class Solution:
    def maxWater(self, arr):   # 👈 naam yahi hona chahiye
        n = len(arr)
        if n < 3:
            return 0
        
        left, right = 0, n - 1
        leftMax, rightMax = arr[left], arr[right]
        water = 0
        
        while left < right:
            if leftMax <= rightMax:
                left += 1
                leftMax = max(leftMax, arr[left])
                water += leftMax - arr[left]
            else:
                right -= 1
                rightMax = max(rightMax, arr[right])
                water += rightMax - arr[right]
        
        return water
        
