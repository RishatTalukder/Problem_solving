def maximum_subarray_sum(arr: list):
    best = 0
    sum = 0

    for i in range(len(input)):
        sum = max(input[i], sum + input[i])
        best = max(best, sum)

    return best
