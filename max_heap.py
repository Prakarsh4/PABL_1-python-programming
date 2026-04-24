import heapq

class Solution:
    def minOperations(self, arr):
        # max heap using negative values
        pq = [-x for x in arr]
        heapq.heapify(pq)
        
        total = sum(arr)
        target = total / 2
        
        operations = 0
        
        while total > target:
            largest = -heapq.heappop(pq)
            
            half = largest / 2
            total -= half
            
            heapq.heappush(pq, -half)
            operations += 1
        
        return operations
