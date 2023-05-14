#Print statement

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