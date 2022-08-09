# 0, 1, 2, 3, 4
# 1, 2, 3, 4, 5
# L     M     R
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while True:
        mid_idx = (left + right) // 2
        mid_el = nums[mid_idx]

        if mid_el == target:
            return mid_idx

        if target > mid_el:
            left = mid_idx + 1
        else:
            right = mid_idx - 1


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))

#Implement an algorithm that finds the index of an element
#in a sorted array of integers in logarithmic time.
#Input                      Output
# -1 0 1 2 4                2
# 1
