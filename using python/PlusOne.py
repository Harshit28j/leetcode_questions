class Solution(object):
    def plusOne(self, digits):
        nums=0
        flag=0
        lst=[]
        arr_len=len(digits)
        count_add=arr_len-1
        for i in range(arr_len):
            nums+=digits[i]*(10**(count_add))
            count_add-=1
        if nums%10==9:
            nums+=1
            flag=1
        if nums%10!=9 and flag==0:
            nums+=1
            print(nums)
        for i in str(nums):
            lst.append(int(i))
        return(lst)