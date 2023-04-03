class AgnosticBin():
	def check_ord(self,lst):
		if (lst[0]<lst[len(lst)-1]):
			return(1)	#ascending order
		else:
			return(0)	#desacending order

	def searchBin(self,lst,tar):
		start=0
		end=len(lst)-1
		while start<=end:
			mid=(start+end)//2

			if self.check_ord(lst)==1:

				if tar>lst[mid]:
					start=mid+1
				elif tar<lst[mid]:
					end=mid-1
				else:
					return(mid)

			elif self.check_ord(lst)==0:
				if tar<lst[mid]:
					start=mid+1
				elif tar>lst[mid]:
					end=mid-1
				else:
					return(mid)

			else:
				return(-1)
		return(-1)


lst=[-2, -1, 0, 1, 2, 9]
tar=2
my_class=AgnosticBin()
sol=my_class.searchBin(lst,tar)
print(sol)