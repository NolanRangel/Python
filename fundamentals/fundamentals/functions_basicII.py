# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]


def countdown(number):
    newList = []
    for i in range(number, 0, -1):
        # print(i)
        newList.append(i)

    return newList


finalCountdown = countdown(5)
print(finalCountdown)


# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def pnr(list):
    # print(list)
    secondNum = None

    for i in range(len(list)):
        # print(i)
        if i >= 1:
            secondNum = list[i]
        elif i < 1:
            print(list[i])

    return secondNum


print(pnr([1, 2]))


# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)


def first_plus_length(list):
    # print(list)
    length = 0
    first_value = None

    for i in range(len(list)):
        # print(i)
        length += 1
        if i < 1:
            first_value = list[i]

    return (first_value + length)


print(first_plus_length([1, 2, 3, 4, 5]))


# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# accept a list and create a new list
# new list contains only values from original list that are greater then its second value
# print how many values this is and then return the new list
# if list has less then 2 elements, return false

def values_greater_than_second(list):
    newList = []
    maxValue = 0
    count = 0

    if len(list) < 2:
        return False

    for i in range(len(list)):
        if i == 1:
            maxValue = list[i]

    for x in range(len(list)):
        if list[x] > maxValue:
            newList.append(list[x])
            count += 1
    print(count)
    return newList


print(values_greater_than_second([5]))


# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

#  accept 2 ints as parameters (size, value)
# create and return a list equal to the given size and whose values are the given value


def length_and_value(size, value):
    newList = []

    for i in range(size):
        newList.append(value)

    return newList


print(length_and_value(6,2))
