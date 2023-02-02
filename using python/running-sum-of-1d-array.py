class Solution(object):
    def runningSum(self, nums):
        ans=[]
        s=0
        for i in nums:
            s+=i
            ans.append(s)
        return(ans)