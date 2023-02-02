class Solution(object):
    def subtractProductAndSum(self, n):
        mul=1
        s_d=0
        while(n!=0):
            s_d+=n%10
            mul=mul*(n%10)
            n=n/10
        return(mul-s_d)