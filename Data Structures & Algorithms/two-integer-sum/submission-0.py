class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            first_num = target - nums[i]
            if first_num in seen:
                return [seen[first_num], i]
            seen[nums[i]] = i
        
        