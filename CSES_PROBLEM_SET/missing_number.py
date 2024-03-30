# import sys 
# import os

# if __name__ == "__main__":
#     if 'LOCAL' in os.environ:
#         sys.stdin = open('input.txt', 'r')
#         sys.stdout = open('output.txt', 'w')

#     n = int(sys.stdin.readline().strip())
#     numbers = list(map(int, sys.stdin.readline().split()))

#     print(sum(range(1, n + 1)) - sum(numbers))


n = int(input())

numbers = list(map(int, input().split()))

stack = list(range(1, n + 1))

for number in numbers:
    stack.remove(number)

print(stack[0])