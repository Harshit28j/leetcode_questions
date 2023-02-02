class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        lst=[]
        m=max(candies)
        for i in candies:
            if i+extraCandies<m:
                lst.append(False)
            else:
                lst.append(True)
        return(lst)