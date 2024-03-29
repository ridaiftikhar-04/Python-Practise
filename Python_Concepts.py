#Print statement

from operator import truediv
from re import T


print("Rida Iftikhar")
print('o.O')
print("-" * 3) #expression

#Exercise: Variables - "We check in a patient named John Smith. He's 20 years old and is a new patient."
patient = 'John Smith'
age = 20
is_new = True
print(patient , "aged" , age , " years is new patient" )  

#Exercise: Input - "Ask two questions from the user."
name = input("What is your name? ")
fav_color = input("What is your favourite color? ")
print(name , 'likes' , fav_color)

#Topic: Type functions i.e., int(), str() etc
#Exercise: "Ask the user their weight(in lbs), convert in Kgs and print on terminal"r
weight_in_pounds = input("What is your weight in pounds? (lbs) : ")
weight_in_kgs = float(weight_in_pounds) * 0.453592
print("Your weight in Kgs is " , weight_in_kgs)

#String Manipulation
#String in Multiple lines
multi_line_string = """Hi John!
Here is our first email to you.

Thank you, 
Support Team
"""
print(multi_line_string)

course = "Python for Beginners"
print(course[:8])
print(course[:]) #a way to clone the string

#Formatted String
first = "John Smith"
last = "the thirdr"
msg = f'{first} ({last}) is a coder'
print(msg)

#String Methods
print(len(course))
print(course.upper())
print(course.endswith("T"))
print(course.find("n"))

#Arithemetic Operations
#Precedence order -> Exponentiation -> Multiplication or Division -> Addition -> Subtraction
x = (2+3) * 10 - 3
print(x)

#Math module
import math
print(math.floor(2.9)) #more detailed functions of pytgon 3 math module @ https://doc.python.org/3/library/math.html

#if else statement
is_hot = True
is_cold = True
if is_hot:
    print("It is a hot day")
    print("Drink Plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes.")
else:
    print("It's a lovely day")
print("Enjoy your day")

#Exercise
is_good_buyer = False
house_price = 1000000
if is_good_buyer:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
    
print(f'Down Payment: ${down_payment}')

#----Lists, Tuples, Sets, Dictionaries----

tuples = ('History' , 'Maths' , 'Art')

#slicing
#remove first item of the tuple and display the rest
tuples1 = tuples[1:] 
print(tuples1)

tuples2 = tuples[:2]
print(tuples2)

#Lists
list1 = ['Urdu', 'Arabic' , 'Turkish']

#add at the end of the list
list1.append('English')
print(list1)

#add at a specific location of the list e.g. 2nd index
list1.insert(2 ,"Korean")
print(list1)

#add another list at the end of a list
list2 = ['Spanish', 'Japanese']
list1.extend(list2)
print(list1)

#remove and return last element of the list
list2.pop()
print(list2)

#sort the list alphabetically or in ascending order
list1.sort()
print(list1)

#sort the list in descending order
list1.sort(reverse = True)
print(list1)

#loop through the list
for index, course in enumerate(list1):
    print(index , course)

#comma separated list
list3 = ','.join(list1)
print(list3)

#split a string and convert each word into list element
split_str = "Split this string into list elements"
new_list = split_str.split(" ")
print(new_list)

#All the values that return False in Python
    # False
    # None
    # Zero to any numeric type
    # Any empty sequence. e.g., "" , (), [].
    # Any empty mapping. e.g., {}.

condition = {}

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

#Loops and iterations
nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print("Number found!")
        continue
    print(num)  

#Nested Loop / Inner loop 
for num in nums:
    for letter in 'abc':
        print(num , letter)

#To iterate to a loop till specific index 
for num in range(7):
    print(num)

#While loop
x = 3
while x<10:
    print(x)
    x = x+1

# y=1
# print("Infinite Loop")
# while True:
#     print(y)
#     y += 1
    
#------Functions--------
def hello_func(greeting, name = 'You'):
    return '{} , {}'.format(greeting, name)

print(hello_func("Hi"))


#Function that accepts arbitrary number of values using * and **
def student_info(*args, **kwargs): 
    print(args)
    print(kwargs)

subjects = ('Maths', 'Art')
info = {'name' : 'John' , 'age' : 24}

student_info(*subjects, **info)

#Doc string: a string like """ test doc """ in a function explaining what the function does

