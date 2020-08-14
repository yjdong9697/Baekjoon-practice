
value_save = []
value = int(input())
n = value
value_save.append(value)

happy_check_dicision = True

while True:
    str_n = str(n)
    n_seperate = list(str_n)
    len_of_n = len(n_seperate)
    temp = 0
    for i in range(len_of_n):
        temp += int(n_seperate[i]) ** 2

    if temp == 1:
        break

    else:

        if temp in value_save:
            happy_check_dicision = False
            break
    
        else:
            value_save.append(temp)
            n = temp

if happy_check_dicision == True:
    print("HAPPY")

else:
    print("UNHAPPY")