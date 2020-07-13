def fib(n):
    """
    :param n: until what value
    :return: fib result
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Function call

num = int(input())

# Result

print(fib(num))