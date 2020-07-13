# Import sys

import sys


# Setting initial value

initial = input()
check = input()
i = 0
count = 0

# Repetition count

while True:
    try:
        if initial[i] == check[0]:
            check_point = True
            for k in range(1,len(check)):
                if initial[i+k] == check[k]:
                    check_point = True
                else:
                    check_point = False
                    break
            if check_point == True:
                count += 1
                i += len(check)
            else:
                i += 1
        else:
            i += 1

    except IndexError:
        break


# Print result

print(count)

# Exit normally

sys.exit(0)