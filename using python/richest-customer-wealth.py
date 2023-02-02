class Solution(object):
    def maximumWealth(self, accounts):
        ans=0
        for wealth in accounts:
            w_c=0
            for i in wealth:
                w_c+=i
                if w_c>ans:
                    ans=w_c
        return(ans)