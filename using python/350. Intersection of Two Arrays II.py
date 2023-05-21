class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        lst = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                lst.append(nums1[i])
                i += 1
                j += 1
        return lst
      
#to run this code locally
# myclass=Solution()
# n1 = [1,2,2,1]
# n2 = [2,2]
# myclass.intersect(n1,n2)
