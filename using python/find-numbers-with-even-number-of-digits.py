class Solution(object):
    def findNumbers(self, nums):
        count=0
        for ele in nums:
            if len(str(ele))%2==0:
                count+=1
        return(count)