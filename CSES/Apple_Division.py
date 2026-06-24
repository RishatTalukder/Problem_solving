n = int(input())
nums = list(map(int, input().split(' ')))

total = sum(nums)
target = total//2

res = float("inf")

def permutation(current, start):
    if start == len(nums):
        return abs(current - (total - current))
    
    if current >= target:
        return abs(current - (total-current))


    return min(
        permutation(current+nums[start], start+1),
        permutation(current, start+1)
    )
    # for i in nums[start:]:
    #     print(f"adding {i}")
    #     current += i

    #     dif = permutation(current, start+1)
    #     # print(res, dif)
    #     res = min(res, dif)

    #     print(f"removing {i}")

    #     current -= i

    # return res

res = permutation(0, 0)

print(res)

