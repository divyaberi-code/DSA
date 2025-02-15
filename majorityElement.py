class Solution(object):
    def majorityElement(self, nums):
        # More voting algorithm
        count = 0
        candidate = 0
        
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                
            if nums[i] == candidate:
                count+=1
            
            else:
                count-=1
        
        return candidate
