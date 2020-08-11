def triangulation(n):
    """
    This function is calculate the triangulation value by recursion
    """

    # Base case

    if n == 3:
        return 0
    
    elif n == 4:
        return 1

    else:
        result = triangulation((n - 1) // 2 + 1) + 2
        save_result[n] = result
        return result

# Initial setting

n = int(input())

save_result = [0] * 1000001
save_result[3] = 0
save_result[4] = 1

# Print result

print(triangulation(n))