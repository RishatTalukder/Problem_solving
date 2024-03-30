import sys
import os

def fast_input():
    return sys.stdin.readline().strip()

def fast_output(data):
    sys.stdout.write(str(data) + '\n')

def main():
    # Your code here
    n = int(fast_input())

    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

    print(n)

if __name__ == "__main__":
    if 'LOCAL' in os.environ:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    main()