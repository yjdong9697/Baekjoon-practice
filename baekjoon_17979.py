import sys

# Default setting

m, n = map(int, sys.stdin.readline().split())

money = [0] * (m + 1)

data = [0] * (n + 1)
data[0] = [None, None, None]
end_data = [0] * 15001

for i in range(15001):
    end_data[i] = []

for i in range(1, m + 1):
    value = int(input())
    money[i] = value

# End data store seperately

for i in range(1, n + 1):
    data[i] = list(map(int, sys.stdin.readline().split()))
    end_data[data[i][1]].append(i)

# Dynamic programming (small to large)

dp = [0] * 15001
initial = 1

while initial <= 15000:
    store = []

    if len(end_data[initial]) == 0:
        dp[initial] = dp[initial - 1]

    else:
        for i in range(len(end_data[initial])):      
            store.append(dp[data[end_data[initial][i]][0]] + (initial - data[end_data[initial][i]][0]) * money[data[(end_data[initial][i])][2]])
        
        # Compare the maximum result and store
        
        if dp[initial - 1] < max(store):
            dp[initial] = max(store)
        else:
            dp[initial] = dp[initial - 1]

    initial += 1

# Print result

print(dp[15000])