class Solution(object):
    def addBinary(self, a, b):
        s_str=''
        num_a=int(a,2)
        num_b=int(b,2)
        s=num_a+num_b
        s_str=(self.binary(s))
        if a=="" and b=="":
            return("0")
        if a=="0" and b=="0":
            return("0")
        else:
            return(s_str)

    def binary(self,x):
        bin_str=''
        while x!=0:
            bin_str+=str(x%2)
            x=x//2
        return(bin_str[::-1])