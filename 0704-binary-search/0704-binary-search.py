class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
        def bs(nums, low, high, target):
             if low > high:
                return -1
 
             mid = (low + high) // 2
               
             if nums[mid] ==  target:
                return mid

             elif target > nums[mid]:
                  return  bs(nums, mid + 1,high,target)
             else:
                 return  bs(nums,low, high -1, target)
            
        return  bs(nums,  0, len(nums) - 1, target)
