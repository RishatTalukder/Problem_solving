sequence = input()

left = 0
right = left+1

mxx = 0

while right < len(sequence):
    if sequence[left] == sequence[right]:
        right += 1

    else:
        mxx = max(mxx, right-left)
        left = right
        right = left+1

mxx = max(mxx, right-left)

print(mxx)
