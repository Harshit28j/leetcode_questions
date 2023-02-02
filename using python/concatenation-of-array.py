class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        a=0
        n=len(nums)*2
        for i in range(0,n):
            ans.append(nums[a])
            a+=1
            if i==len(nums)-1:
                a=0
        return(ans)


# Alternative with 98% beats
# class Solution(object):
#     def getConcatenation(self, nums):
#         return nums*2