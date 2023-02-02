class Solution:
    def romanToInt(self, s):
        di_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        s_len=len(s)
        value=0
        for i in range(s_len):
            if s[i] in di_roman.keys():
                value+=di_roman[s[i]]
        return(value)