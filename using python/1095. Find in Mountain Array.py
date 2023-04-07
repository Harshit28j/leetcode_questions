class MountainArray(object):
   def get(self, index):
       """
       :type index: int
       :rtype int
       """

   def length(self):
       """
       :rtype int
       """
class Solution(object):
    def findInMountainArray(self,target, mountain_arr):
        len_arr = mountain_arr.length()
        peak_index = self.find_peak_index(mountain_arr, len_arr)

        # search in the ascending half of the array
        left = 0
        right = peak_index
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1

        # search in the descending half of the array
        left = peak_index
        right = len_arr - 1
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                right = mid - 1
            else:
                left = mid + 1

        return -1  # target not found


    def find_peak_index(self,arr, l):
        left = 0
        right = l - 1
        while left < right:
            mid = (left + right) // 2
            if arr.get(mid) < arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        return left
