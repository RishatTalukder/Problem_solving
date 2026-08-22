from sys import stdin

input = stdin.readline

n, m, k = map(int, input().strip().split())

applicants = list(map(int, input().strip().split()))

apertments = list(map(int, input().strip().split()))

print()

def solve(applicants, apertments):
    # print(len(apertments))
    applicants.sort()
    apertments.sort()

    count = 0

    required_ind = 0
    size_ind = 0

    while required_ind < n and size_ind < m:
        required = applicants[required_ind]
        size = apertments[size_ind]

        if size < required - k:
            size_ind += 1

        elif size > required + k:
            required_ind += 1

        else:
            count += 1
            size_ind += 1
            required_ind += 1

    return count

print(solve(applicants, apertments))