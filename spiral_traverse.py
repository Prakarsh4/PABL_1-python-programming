class Solution:
    def spirallyTraverse(self, mat):
        res = []
        n, m = len(mat), len(mat[0])
        
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        
        while top <= bottom and left <= right:
            
            # top row
            for i in range(left, right + 1):
                res.append(mat[top][i])
            top += 1
            
            # right column
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1
            
            # bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(mat[bottom][i])
                bottom -= 1
            
            # left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1
        
        return res
