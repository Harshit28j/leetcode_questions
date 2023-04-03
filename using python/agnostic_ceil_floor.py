class sol():
	def check_ord(self,lst):
		if (lst[0]<lst[len(lst)-1]):
			return(1)	#ascending order
		else:
			return(0)	#desacending order

	def ceil_num(self,lst,tar):
		start=0
		end=len(lst)-1
		while start<=end:
			mid=(start+end)//2
			if self.check_ord(lst)==1:#ascending order

				if tar>lst[mid]:
					start=mid+1
				elif tar<lst[mid]:
					end=mid-1
				else:
					return(lst[mid])
				ch=start

			elif self.check_ord(lst)==0:#desacending order
				if tar<lst[mid]:
					start=mid+1
				elif tar>lst[mid]:
					end=mid-1
				else:
					return(lst[mid])
				ch=end

		return(lst[ch])

	def floor(self,lst,tar):
		start=0
		end=len(lst)-1
		while start<=end:
			mid=(start+end)//2
			if self.check_ord(lst)==1:#ascending order

				if tar>lst[mid]:
					start=mid+1
				elif tar<lst[mid]:
					end=mid-1
				else:
					return(lst[mid])
				ch=end


			elif self.check_ord(lst)==0:#desacending order
				if tar<lst[mid]:
					start=mid+1
				elif tar>lst[mid]:
					end=mid-1
				else:
					return(lst[mid])
				ch=start


		return(lst[ch])

#arrays of both order to test
# lst=[9, 2, 0, -1, -2]
lst=[-2, -1, 0, 1, 2, 9]
tar=5
my_class=sol()
sol=my_class.ceil_num(lst,tar)
sol2=my_class.floor(lst,tar)
print(sol,sol2)
