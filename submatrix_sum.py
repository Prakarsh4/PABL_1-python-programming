class Solution:
    def submatrixSum(self, n, m, a, q, query):
        
        # Step 1: prefix sum matrix
        ps = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                ps[i][j] = a[i][j]
                
                if i > 0:
                    ps[i][j] += ps[i-1][j]
                if j > 0:
                    ps[i][j] += ps[i][j-1]
                if i > 0 and j > 0:
                    ps[i][j] -= ps[i-1][j-1]
        
        # Step 2: answer queries
        res = []
        
        for i in range(q):
            x1, y1, x2, y2 = query[i]
            
            total = ps[x2][y2]
            
            if x1 > 0:
                total -= ps[x1-1][y2]
            if y1 > 0:
                total -= ps[x2][y1-1]
            if x1 > 0 and y1 > 0:
                total += ps[x1-1][y1-1]
            
            res.append(total)
        
        return res
