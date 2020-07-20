import sys

check = False
result = []

while not check:
    data = list(map(int, sys.stdin.readline().split()))
    count = 0
    if data == [-1]:
        check = True
        break

    else:
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] * 2 == data[j] or data[i] / 2 == data[j]:
                    count += 1

        result.append(count)


for i in range(len(result)):
    print(result[i])
