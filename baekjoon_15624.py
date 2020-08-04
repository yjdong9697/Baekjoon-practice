import sys

n = int(input())
fib_store = [0] * (2)

fib_store[0] = 0
fib_store[1] = 1

for i in range(n - 1):
    temp = fib_store[1]

    fib_store[1] = (fib_store[0] + fib_store[1]) % 1000000007
    fib_store[0] = temp

if n == 0:
    print(0)

else:
    print(fib_store[1] % 1000000007)
