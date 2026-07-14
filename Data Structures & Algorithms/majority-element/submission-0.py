class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        max_count = res = 0

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > max_count:
                max_count = count_dict[num]
                res = num
        return res

        