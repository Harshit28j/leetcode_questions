# time complexity of this program is O(m*n)
# class Solution:
#     def searchMatrix(self, matrix, target):
#         for i in range(0,len(matrix)):
#             if target in matrix[i]:
#                 return(True)

class Solution:
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
#time complexity of above program is O(log(m) + log(n))
      
