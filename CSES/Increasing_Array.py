n = int(input())

nums = list(map(int, input().split(' ')))

if n <= 1:
    print(0)
    exit()

res = 0

for i, val in enumerate(nums):
    if i > 0 and val < nums[i-1]:
        res += nums[i-1] - val
        nums[i] = nums[i-1]
        
    # print(res)


print(res)