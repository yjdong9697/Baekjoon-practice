import sys

result_data = []

while True:  
    L, P, V = map(int, sys.stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
        break

    else:
        if V % P > L:
            result = (V // P) * L + L
        
        else:
            result = (V // P) * L + V % P

    result_data.append(result)


for i in range(len(result_data)):
    print("Case "+str(i + 1)+": "+str(result_data[i]))