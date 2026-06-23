# my version, looks a little bruteforce
from collections import Counter
import math

string = input()

n = len(string)

odd = n%2

count = Counter(string)

odd_count = 0

odd_key = ''

for i in count:
    if count[i]%2 == 1 and odd:
        odd_count += 1
        if odd_count > 1:
            print("NO SOLUTION")
            exit()

        odd_key = i

    elif not odd and count[i]%2==1:
        print("NO SOLUTION")
        exit()


left = ""
right = ""

for i in count:
    if i != odd_key:
        left += i*(count[i]//2)
        right += i*(count[i]//2)

    else:
        left += i*math.floor(count[i]//2)
        right += i*math.floor(count[i]//2)

print(left + odd_key + right[::-1])


# clean version
from collections import Counter

string = input()

count = Counter(string)
odd_chars = []

for char, freq in count.items():
    if freq % 2 == 1:
        odd_chars.append(char)

if len(odd_chars) > 1:
    print("NO SOLUTION")
    exit()

middle = odd_chars[0] if odd_chars else ""

left = ""

for char, freq in count.items():
    left += char * (freq // 2)

result = left + middle + left[::-1]

print(result)

