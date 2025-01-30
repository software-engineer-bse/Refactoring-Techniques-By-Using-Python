list_1 = [4,2,3,1]

def list_calculations(list_1):
    # Sum of list elements
    sum = 0
    for i in list_1:
        sum = sum + i
    print(sum)

    # Multiply list elements
    multiply = 1
    for j in list_1:
        multiply = multiply*j
    print(multiply)

list_calculations(list_1)