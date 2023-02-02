class Solution(object):
    def shuffle(self, nums, n):
        arr=[]
        for i in range(0,len(nums)//2):
            arr.append(nums[i])
            arr.append(nums[len(nums)//2+i])
        return(arr)