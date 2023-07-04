def array_sum(nums, idx):
    if idx == len(nums) - 1:  # base case - tova e danoto
        return nums[idx]
    return nums[idx] + array_sum(nums, idx + 1)


numbers = [int(x) for x in input().split()]

print(array_sum(numbers, 0))
