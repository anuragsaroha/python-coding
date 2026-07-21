"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

from typing import List

def search_insert(nums: List[int], target: int) -> int:
    # Handle empty array
    if not nums:
            return -1

    # If target is greater than the last element, insert at the end
    if target > nums[-1]:
        return len(nums)

    # Initialize binary search pointers
    left, right = 0, len(nums) - 1
    
    # Perform binary search
    while left < right:
        # Calculate mid index to avoid overflow
        mid = (left + right) // 2
        
        # If middle element is less than target, search right half
        if nums[mid] < target:
            left = mid + 1
        # Otherwise, search left half (mid could be the insertion point)
        else:
            right = mid
    
    # Return the insertion index
    return left


# Test cases

def main():
    test_cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ]

    for nums, target, expected in test_cases:
        result = search_insert(nums, target)
        assert result == expected, f"Failed for nums={nums}, target={target}. Expected {expected}, got {result}"
        print(f"Passed for nums={nums}, target={target}. Expected and got {expected}")

if __name__ == "__main__":
    main()