class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count_dict = {}
        # for i in range(len(nums)):
        #     if nums[i] in count_dict:
        #         ret  
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        return True   