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


string = list(input())

permute(string, 0)

print(len(res))
print(*sorted(res), sep="\n")


