import sys

N, K = map(int, sys.stdin.readline().split())

N_data = []


# Input N_data (make list)

for i in range(N):
    data = int(input())
    N_data.append(data)

# Calculate Inversely

count = 0
for i in range(1,11):

    # If K == 0 makes early (break) 

    if K == 0:
        break

    if K >= N_data[-i]:
        count += K // N_data[-i]
        K = K % N_data[-i]
        
# Print the result
    
print(count)