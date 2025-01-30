list_1 = [4,2,3,1]

def list_calculations(list_1):
    # Sum of list elements
    sum = sum_list_elements(list_1)
    print(sum)

    # Multiply list elements
    multiply = multiply_list_elements(list_1)
    print(multiply)


def sum_list_elements(list):
    sum = 0
    for i in list:
        sum = sum + i
    return(sum)


def multiply_list_elements(list):
    multiply = 1
    for i in list:
        multiply = multiply*i
    return multiply


list_calculations(list_1)