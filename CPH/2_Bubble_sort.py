def bubble_sort(input: list):
    for i in range(len(input)):
        for j in range(len(input)-1):
            if input[j] > input[j + 1]:
                input[j], input[j + 1] = input[j + 1], input[j]

    return input
