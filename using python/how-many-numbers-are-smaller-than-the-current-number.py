class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # min_m=min(nums)
        count=0
        lst=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[j]<nums[i]:
                    count+=1  
            lst.append(count)
            count=0
        return(lst)