nums = [int(x) for x in input().split()]

for i in range(len(nums)):
    for j in range(1, len(nums) - i):
        if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

print(*nums, sep=" ")

#------------------------------ANOTHER SOLUTION------------------------------

nums = [int(x) for x in input().split()]

is_sorted = False
counter = 0
while not is_sorted:
    is_sorted = True
    for idx in range(1, len(nums) - counter):
        if nums[idx] < nums [idx - 1]:
            nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
            is_sorted = False
    counter += 1

print(*nums, sep=" ")

#Write an implementation of Bubble Sort. You should read an array of integers and sort them.
#Input                          Output
# 5 3 1 2 4                     1 2 3 4 5
