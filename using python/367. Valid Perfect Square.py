class Solution:
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        
        low = 1
        high = num
        
        while low <= high:
            mid = (low + high) // 2
            sqr = mid * mid
            
            if sqr == num:
                return True
            elif sqr < num:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

#to run script locally in your system
# myclass=Solution()
# n=5
# print(myclass.isPerfectSquare(n))
