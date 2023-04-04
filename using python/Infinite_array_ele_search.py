import numpy as np
class Infinite_array():
	def searchBin(self,lst,tar):
		start=0
		end=1
		while (tar>lst[end]):
			start_new=end+1
			end=end+(end-start+1)*2
			mid=(start+end)//2

		while (start<=end):
			mid=start+(end-start)//2
			if tar>lst[mid]:
				start=mid+1
			elif tar<lst[mid]:
				end=mid-1
			else:
				return(mid)
		return(-1)


lst=np.arange(-100000,100000) #consider this infinite 
tar=45852
my_class=Infinite_array()
sol=my_class.searchBin(lst,tar)
print(sol)
