class Solution(object):
    def search(self, nums, target):
        s=0
        end=len(nums)-1
        if target==nums[s]:
            return(s)
        while(s<=end):
            mid=(s+end)//2
            if nums[mid]<target:
                s=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                return(mid)

        return(-1)

#to run locally
# myclass=Solution()
# n=[2,5]
# print(myclass.search(n,5))

