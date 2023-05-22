class Solution:
    def findMin(self, nums):
        s, end = 0, len(nums)-1
        while s < end:
            mid = (s + end) // 2         
            if nums[mid] > nums[end]:
                s = mid + 1
            else:
                end -=1 
                
        return(nums[s])
