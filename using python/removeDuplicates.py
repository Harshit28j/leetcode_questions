class Solution(object):
    def removeDuplicates(self, nums):
    	for elements in nums:
    		while nums.count(elements)>1:
    			nums.remove(elements)
    	return(len(nums))