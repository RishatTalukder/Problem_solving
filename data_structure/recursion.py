
def sum(a):
    if a > 50:
        return
    summ = a + 1
    sum(summ)
    return summ

summ = sum(0)

print(summ)