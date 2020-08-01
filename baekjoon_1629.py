import sys

A, B, C = map(int, sys.stdin.readline().split())

remain_first = A % C

# A ** n = A ** (n - 1) * A = (C * n + remain1) * (C + m + remain2)
# So, the result is same as calcaulte remainder (By using divide and conquer)

def multiplier(remain, above):
    if above == 1:
        return remain
          
    if above % 2 == 0:
        return (multiplier(remain, above // 2) ** 2) % C

    else:
        return (multiplier(remain, above // 2) ** 2 * multiplier(remain, 1)) % C

# Print result

print(multiplier(remain_first, B))