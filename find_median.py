class Solution:
    def findMedian(self, arr):   # 👈 EXACT naam
        arr.sort()
        n = len(arr)
        
        if n % 2 == 1:
            return arr[n // 2]
        else:
            return (arr[n // 2] + arr[n // 2 - 1]) / 2
