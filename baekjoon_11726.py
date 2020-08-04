import sys

def paint(n):
    """
    If data is exist in paint_store : divide and conquer
    not exist : calculate and store
    """
    # Early exit

    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    # else

    else:
        if paint_store[n - 1] == 0:
            paint(n - 1)
        
        result = paint_store[n - 1] + paint_store[n - 2]
        paint_store[n] = result

        return result
        
# Initial setting

n = int(input())
paint_store = [0] * (n + 2)
paint_store[1] = 1
paint_store[2] = 2

# Print the result

print(paint(n) % 10007)