nums = [int(x) for x in input().split()]

for idx in range(len(nums)):
    min_number = nums[idx]
    min_idx = idx
    for next_idx in range(idx + 1, len(nums)):
        next_number = nums[next_idx]
        if next_number < min_number:
            min_number = next_number
            min_idx = next_idx
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

print(nums)

#Write an implementation of Selection Sort. You should read an array of integers and sort them.
#Input                 Output
#5 4 1 3 2             1 2 3 4 5
