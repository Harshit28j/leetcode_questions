class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    if i < j:
                        count += 1
        return count
