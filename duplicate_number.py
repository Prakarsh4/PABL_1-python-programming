"""class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow"""
n = int(input())
arr = list(map(int, input().split()))

freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
max_count = 0
result = arr[0]
for num in freq:
    if freq[num] > max_count:
        max_count = freq[num]
        result = num

print(result)