def findNthDigit(n: int) -> int:
        dig = rang = 1

        while n > 9*rang*dig:
            n-= 9*rang*dig
            dig += 1
            rang *= 10


        passed, position = divmod((n-1),dig)
        target = str(rang+passed)[position]

        return int(target)


n = int(input())

for i in range(n):
    print(findNthDigit(int(input())))