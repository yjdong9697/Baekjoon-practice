import sys

N = int(input())

P_list = list(map(int, sys.stdin.readline().split()))

P_list.sort()

# Calculate sum

sum = 0

for i in range(N):
    sum += P_list[i] * (N - i)

# Print result

print(sum)