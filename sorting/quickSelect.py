#  215. Kth largest
# Solution using quick select **partition**
# ref: wiki https://en.wikipedia.org/wiki/Quickselect
# also see CLRS

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        return self.findKthSmallest(nums, len(nums)+1-k)
        
    def findKthSmallest(self, nums, k):
       if nums: 
           # try randomized pivot index
           
            pivotIdx = random.randint(0,len(nums)-1)
           
            pivot = self.partition(nums, 0, len(nums)-1, pivotIdx)
            
            if pivot +1> k:
                
                # search for smaller indices
                
                return self.findKthSmallest(nums[:pivot], k)
                
            elif pivot +1< k:
                
                return self.findKthSmallest(nums[pivot+1:], k-pivot-1)
            else:
                return nums[pivot]
            
    def partition(self, nums, l, r, pivotIndex):
        pivotVal = nums[pivotIndex]
        nums[r], nums[pivotIndex] = nums[pivotIndex],nums[r]
        lo = l
        while l<r:
            
            if nums[l] < pivotVal:
                
                nums[lo], nums[l] = nums[l], nums[lo]
                lo +=1
                
            l += 1
            
        nums[r], nums[lo] = nums[lo], nums[r]
        return lo
