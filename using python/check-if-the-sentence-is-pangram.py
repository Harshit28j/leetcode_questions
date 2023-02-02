class Solution(object):
    def checkIfPangram(self, sentence):
        count=0
        str_A='abcdefghijklmnopqrstuvwxyz'
        for i in range(0,len(str_A)):
            if str_A[i] in sentence:
                count+=1
        if count==26:
            return(True)
        else:
            return(False)
            
