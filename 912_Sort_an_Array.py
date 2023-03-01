# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
from typing import List


def sortArray(nums: List[int]) -> List[int]:
    def merge(a, b):
        idx_a, idx_b = 0, 0
        merged = []
        while idx_a < len(a) and idx_b < len(b):
            if a[idx_a] > b[idx_b]:
                merged.append(b[idx_b])
                idx_b += 1
            else:
                merged.append(a[idx_a])
                idx_a += 1
        if idx_a < len(a):
            merged.extend(a[idx_a:])
        else:
            merged.extend(b[idx_b:])
        return merged

    def sort(arr):
        n = len(arr)
        if n == 1:
            return arr
        a = sort(arr[: n // 2])
        b = sort(arr[n // 2 :])
        return merge(a, b)

    return sort(nums)


if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    print(sortArray(nums))
