def pas(n, m):
    """
    Find the value of (n,m) pascal
    """

    # First low

    if n == 1:
        return 1

    # side value == 1

    elif m == 1 or n == m:
        return 1

    # special value 1

    elif m == 2 or m == n-1:
        return n-1

    # special value 2

    elif m == 3 or m == n-2:
        sum_type = 0
        for i in range(1, n-1):
            sum_type += i
        return sum_type

    # Else value

    else:
        sum_value = 0
        for i in range(1, m+1):
            sum_value += pas(n-i, m-i+1)

        return sum_value


# Input value and initial setting

x = input()
x_split = x.split()
n = int(x_split[0])
m = int(x_split[1])


# Print the result

print(pas(n, m))