# # Single Element in a Sorted Array
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.


def non_duplicate(nums: list) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        if low == high:
            return nums[low]
        mid = (high + low) // 2
        if nums[mid] == nums[mid + 1]:
            if mid % 2 == 0:
                low = mid + 1
            else:
                high = mid
        elif nums[mid] == nums[mid - 1]:
            if mid % 2 == 0:
                high = mid
            else:
                low = mid + 1
        else:
            return nums[mid]


print(non_duplicate([1, 1, 2, 3, 3]))
