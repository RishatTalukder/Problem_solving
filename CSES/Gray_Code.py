n = int(input())

count = 1

res = ["0", "1"]

while count < n:
    added_bit_0 = list(map(lambda x: "0"+x, res))

    added_bit_1 = list(map(lambda x: "1"+x, res[::-1]))

    res = added_bit_0 + added_bit_1
    count += 1

print(*res, sep="\n")