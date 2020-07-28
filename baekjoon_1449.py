import sys

N, L = map(int, sys.stdin.readline().split())

# Input N data

N_data = list(map(int,sys.stdin.readline().split()))
N_data.sort()

# Calculate

count = 0
start = N_data[0] - 0.5
for i in range(N):
    
    # Some interval is overlap

    if N_data[i] + 0.5 > start >= N_data[i] - 0.5:
        start += L
        count += 1
            
    # Completely overlap

    elif start >= N_data[i] + 0.5:
        try:
            if start <= N_data[i + 1] - 0.5:
                start = N_data[i + 1] - 0.5
        except IndexError:
            break
    
    # Completely not overlap

    elif start < N_data[i] - 0.5:
        count += 1
        start = N_data[i] - 0.5 + L

# Print result

print(count)
