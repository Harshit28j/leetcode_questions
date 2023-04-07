class Solution(object):
	def peak(self,arr):
		
		start=0
		end=len(arr)-1
		while(start<=end):
			mid=(start+end)//2
			if (mid<end and arr[mid]>arr[mid+1]):
				return(mid)
			elif (mid>start and arr[mid]<arr[mid-1]):
				return(mid-1)
			elif (arr[mid]<=arr[start]):
				end=mid-1
			else:
				start=mid+1
		return(-1)
	def bin(self,nums,target,start,end):
		while(start<=end):
				mid=(start+end)//2
				if target<nums[mid]:
						end=mid-1
				elif target>nums[mid]:
						start=mid+1
				else:
						return(mid)
		return(-1)

	def search(self,nums,target):
		arr=nums
		pivot=self.peak(arr)
		if pivot==-1:
			return(self.bin(arr,target,0,len(arr)-1))
		if (arr[pivot]==target):
			return(pivot)
		if(target>=arr[0]):
			return(self.bin(arr,target,0,pivot-1))
		return(self.bin(arr,target,pivot+1,len(nums)-1))
