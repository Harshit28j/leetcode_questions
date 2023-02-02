class Solution(object):
    def createTargetArray(self, nums, index):
        tar=[]
        for i in range(len(nums)):
            tar.insert(index[i],nums[i])
        return(tar)