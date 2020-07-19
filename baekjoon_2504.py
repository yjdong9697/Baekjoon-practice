import sys

# Data input

data = list(map(str, sys.stdin.readline()))
data_store = []

# Error catch boolean flag

error = False

for i in range(len(data)-1):
    if data[i] == ")":
        if "(" in data_store:

            # Find last "("

            start_1 = - 1
            while True:
                if data_store[start_1] == "(":
                    find_index = len(data_store) + start_1
                    break
                else:
                    start_1 += -1

            data_store[find_index] = 2
            sum_of_data_1 = 0
            initial = 1

            # Consider inside "( )"

            try:
                while True:
                    sum_of_data_1 += int(data_store.pop(find_index + initial))

            except IndexError:
                pass

            # In () if exist any "[" or "]" : raise error

            except ValueError:
                error = True

            if sum_of_data_1 == 0:
                data_store[find_index] = 2
            else:
                data_store[find_index] = 2 * sum_of_data_1

        else:
            error = True

    elif data[i] == "]":
        if "[" in data_store:

            # Find last "["

            start_2 = - 1
            while True:
                if data_store[start_2] == "[":
                    find_index = len(data_store) + start_2
                    break
                else:
                    start_2 += -1
            data_store[find_index] = 3
            sum_of_data_2 = 0
            initial = 1

            # Consider inside "[ ]"

            try:
                while True:
                    sum_of_data_2 += int(data_store.pop(find_index + initial))

            except IndexError:
                pass

            # In [] if exist any "(" or ")" : raise error

            except ValueError:
                error = True

            if sum_of_data_2 == 0:
                data_store[find_index] = 3
            else:
                data_store[find_index] = 3 * sum_of_data_2

        else:
            error = True

    # Default cases : append the data to data_store

    else:
        data_store.append(data[i])

# Error checker (if error is raise : print 0)

if error:
    print(0)

# Sum of the remainder

else:
    try:
        result_sum = 0
        for i in range(len(data_store)):
            result_sum += data_store[i]

        print(result_sum)

    # if exist "[" or "(" alone : raise error and print 0

    except TypeError:
        print(0)
