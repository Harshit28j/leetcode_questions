class Solution(object):
    def searchInsert(self, nums, target):
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=(start+end)//2
            if target>nums[mid]:
                start=mid+1
            elif target<nums[mid]:
                end=mid-1
            else:
                return(mid)
        if target in nums:
            return(end)
        else:
            return(end+1)

#to run this locally
#myclass=Solution()
#lst=[1,3,5,6]
#target=6
#print(myclass.searchInsert(lst,target))
