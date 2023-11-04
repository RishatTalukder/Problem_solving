from collections import Counter

def suss(s):
    num = len(s)
    count1 = Counter(s[0:num//2])
    count2 = Counter(s[num//2:])
    
    if num == 2:
        if s[0] == s[1]:
            return 0

        else:
            return 1

    if count1["0"] >= count1["1"]:
        changes1 = count1["1"]

    else:
        changes1 = count1["0"]

    if count2["0"] >= count2["1"]:
        changes2 = count2["1"]

    else:
        changes2 = count2["0"]

    return changes1 + changes2

print(suss("11000111"))