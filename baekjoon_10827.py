import sys

n, x = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

for i in range(len(data)):
    if data[i] < x:
        print(data[i], end = " ")