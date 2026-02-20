class Solution:
    def prevSmaller(self, arr):
        stack = []
        result = []

        for x in arr:
            # pop all greater or equal elements
            while stack and stack[-1] >= x:
                stack.pop()

            # if stack empty → no smaller element
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])

            # push current element
            stack.append(x)

        return result
