# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


def search(nums: list, target: int) -> int:
    """Find target in sorted list nums. 
    Returns the index of the first instance of target or an index i such that
    target >= nums[i:].

    Args:
        nums (list): Sorted list to search.
        target (int): Element to find.

    Returns:
        int: Index i such that target >= nums[i:].
    """
    low = 0
    high = len(nums)

    while low < high:
        print(low, high)
        mid = (high + low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


# Example
print(search([1, 2, 3, 3], 3))
