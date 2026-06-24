from collections import Counter

res = []

cache = set()

def permute(string, current):
    if current == len(string):
        res.append(''.join(string))
        return
    
    used = set()
    
    for i in range(current, len(string)):
        if string[i] in used:
            continue

        used.add(string[i])

        string[current], string[i] = string[i], string[current]
        
        permute(string, current+1)

        string[current], string[i] = string[i], string[current]


# frequency
def frequency_permute(current):
    if len(current) == len(string):
        res.append(''.join(current))
        return
    
    for i in sorted(freq.keys()):
        if freq[i] == 0:
            continue

        current.append(i)

        freq[i] -= 1

        frequency_permute(current)

        freq[i] += 1
        current.pop()


string = list(input())

freq = Counter(string)

# permute(string, 0)
frequency_permute([])


print(len(res))
print(*sorted(res), sep="\n")


