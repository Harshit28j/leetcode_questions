class Solution():
	def peakIndexInMountainArray(self,lst):
		start=0
		end=len(lst)-1
		while(start<end):
			mid=start+(end-start)//2
			if lst[mid]>lst[mid+1]: #at decreasing side of array
				end=mid
			else: #at increasing side of array 
				start=mid+1
		return(start)
