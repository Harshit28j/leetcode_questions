class Solution(object):
    def isPalindrome(self, x):
        return str(x)[::-1] == str(x)

myclass=Solution()
x=121
print(myclass.isPalindrome(x))
