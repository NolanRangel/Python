num1 = 42   # variable declaration/data type number/primitive
num2 = 2.3  # variable declaration/data type float/primitive
boolean = True  # variable declaration/data type boolean/primitive
string = 'Hello World'  # variable declaration/data type string/primitive
# List/initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# Dictionary/initialize
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}
# Tuple/initialize
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))  # type check
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')  # list/addvalue
print(person['name'])  # dictionary/acces value
person['name'] = 'George'  # dictionary/change value
person['eye_color'] = 'blue'
print(fruit[2])  # log statement

if num1 > 45:       # conditional/if
    print("It's greater")
else:                  # conditional/else
    print("It's lower")

if len(string) < 5:  # length check
    print("It's a short word!")
elif len(string) > 15:  # length check/conditional/else if
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):  # for loop/stop
    print(x)  # for loop/stop
for x in range(2, 5):  # for loop/ start,stop
    print(x)
for x in range(2, 10, 3):  # for loop/ start,stop,step(increment)
    print(x)
x = 0  # while/start
while(x < 5):  # while/stop
    print(x)
    x += 1  # while/increment

pizza_toppings.pop()
pizza_toppings.pop(1)  # list/delete value

print(person)
person.pop('eye_color')  # dictionary/delte value
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue  # for loop/continue
    print('After 1st if statement')
    if topping == 'Olives':
        break  # for loop/break


def print_hello_ten_times():  # funtion
    for num in range(10):
        print('Hello')


print_hello_ten_times()


def print_hello_x_times(x):  # function/parameter
    for num in range(x):
        print('Hello')


print_hello_x_times(4)  # function/argument/return


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


# print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section       #comment multiline
"""

# print(num3)           #comment single line
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
name = "Zen"
print("My name is", name)


name = "Zen"
print("My name is " + name)
