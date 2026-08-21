
 print("*"*10)
    #!The '*' function multiplies(repeats) the given variable the said number of times when giving output

# n = input('''What is your name?'''  )
    #! The (''') are used to format the block of texts in multiple lines like writing a message

# c=input("What is your favourite colour? ")
# print(n + " likes " + c)
    #! The "+" symbol is used to combine multiple inputs(strings) to print one single output

# b=(input("Birth Year: "))
    #! the input() function always returns the user's input as a string data type

# a=2026-int(b)
    #! Only a float or an integer can be subtracted from a number so the string has to be converted to an integer

# if a<18:
    # print('Sorry, You are not eligible to vote')
# else:
    # print('You are elegible to vote!')
# print("Your age is " + str(a) + " and your favoourite colour is " + c)
    #! When using the "+" symbol to print multiple variables together they must be converted back to string, adding an integer to a string wil result in error

# g='Guide for Beginners'
# print(g[0:5])
    #! The [x:y] function prints the charactes of the variable from X(first charecter is counted as 0) to the (y-1)th character

# print(g)
# print(g.upper())
# print(g.lower())
# print(g.find('B'))
# (print(g.replace('Beginners','Pros'))
    #! The methods(.upper, .lower, .find, .replace) are functions specific to string type variables

# print('Guide' in g)
    #! This function is used to check whether a word or a chracter is present in the variable. The output to this function is a boolean value i.e. True/False

# first_name='Nat'
# middle_name='De'
# ast_name='Salvia'
# print(first_name+" [" + middle_name +"] " + last_name)
# first_name=input('Enter First Name: ')
# middle_name=input('Enter Middle Nmae: ')
# last_name=input('Enter Last Name: ')
# print(first_name+ " [" + middle_name +"] " + last_name)
# User_Name=f'{first_name} [{middle_name}] {last_name}'
    #! The f(formated string) funtion is used to simplify the code to avoid multple parantheses, it fetches the values of the variables directly into the brackets

# print('The User Name is ' + User_Name)
# print("The number of characters in the User's Name is " + str(len(User_Name)))
    #! The len() function is use to count the no of charaters in the variable

# x=-4.5
# print(round(x))
    #! round() functins rounds of the no to the nearest integer

# print(abs(x))
    #! abs() function reports the absolute(modulus) value of the number

# import math
# print(math.ceil(x))
    #! https://docs.python.org/3/library/math.html

# i=1
# while i<=5:
#     print(i)
#     i=i+1
# print('Done!')
    #! while loop will repeat a chain of commands until the intial conditions are met

# Name=("Python")
# for characters in Name:
#     print(characters)
    #! A string is a sequence of characters, so for can iterate through it one character at a time. Python sees the sting as: "" "" "" ""...
# price= [10,20,30]
# total=0
# for item in price:
# print(f'Total price: {total}')
    #! for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or any other iterable object(It executes the block of code once for each item in the sequence)

# for x in range(4):
#     for y in range(4):
#         print(f'[{x},{y}]')
    #! Nested loop is a loop placed inside the body of another loop.  The inner loop runs completely for every single iteration of the outer loop.

# name=['Carol','Misery','Jonathron','Aria']
# print(name[0:2])
    #! The individual elements from the list can be accessed by specifying the ranking or the range of elements

# matrix=[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][1])
    #! 2D list are the lists inside another list and their elements can be extracted using double coordinates; group[α][β]

# numbers=[5, 2, 1, 7, 4 ]
# numbers.insert(1,20)
    #! https://docs.python.org/3/tutorial/datastructures.html
# print(numbers)
# print(numbers.index(5))
    #! Shows error for a value not available in the list
# print(50 in numbers)
    #! Does not show error

# numbers=(1, 2, 3)
    #! Data stored in parantheses(tuple object) does not support item assignment and cannot be modified.

# coordinates=(1, 2, 3)
# x, y, z=coordinates
# print(x)
    #! Unpacking allows to extract individual elements from iterables (like tuples or lists) and assign them to separate variables in a single statement.

# customer={
#     "name":"Flower Child",
#     "age":28,
#     "is_verified":True
# }
# print(customer["name"])
    #! Dictionary is a built-in data structure used to store data in key:value pairs. It is mutable in nature

# def greet_user(name):
#     print(f'Hi {name}!')
#     print('Welcome aboard')
# print('Start')
# greet_user('Dick')
# print('Finish')
    #! def keyword is used to create a user-defined function, which is a reusable block of code that runs only when called.
    #! Parameters are used to recieve information in the function.

# def square(number):
#     return (number*number)
# print(square(3))
    #! return keyword is used inside a function to exit that function and send a calculated result back to the code that called it.

# try:
#     age=int(input('Age:'))
# except ValueError:
#     print('Invalid Value!')
    #! "try" and "except" blocks are used to handle runtime errors (exceptions) gracefully, ensuring your application doesn't crash unexpectedly.

class Point:
    def move(self):
        print('Move')
    def draw(self):
        print('Draw')
point1=Point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()
    #! A class is a reusable template or blueprint used to build objects, which are distinct instances encapsulating both data (attributes) and behaviors (methods)
