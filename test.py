from collections import OrderedDict, Counter

nums = [3,0,1,0,2]

nums_count = OrderedDict(sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True))
nums_count_ordered = OrderedDict(Counter(nums))

print(nums_count)
print(nums_count_ordered)