input()
nums = list(map(int, input().split())) 

before = 0
after = 1

summ = 0

while after < len(nums):
    if nums[before] > nums[after]:
        summ = summ + nums[before] - nums[after]
        nums[after] = nums[before]
    else:
        before = after
    after += 1


print(summ)