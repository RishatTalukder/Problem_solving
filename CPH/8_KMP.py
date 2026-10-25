def kmp(text: str, pattern: str) -> int:
    if not pattern:
        return 0

    # Build the LPS (Longest Proper Prefix which is also Suffix) array
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search for the pattern in the text
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                return i - j
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


def kmp(nums1, nums2):
    n,m  = len(nums1), len(nums2)

    pi = [0]*m
    j = 0

    for i in range(1, m):
        while j > 0 and nums2[i] != nums2[j]:
            j = pi[j-1]

        if nums2[i] == nums2[j]:
            j += 1

        pi[i] = j


    j = 0

    for i in range(n):
        while j > 0 and nums1[i] != nums2[j]:
            j = pi[j-1]

        if nums1[i] == nums2[j]:
            j += 1

        if j == m:
            return True


    return False