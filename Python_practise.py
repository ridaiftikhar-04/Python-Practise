#practise
#Module

import my_module as mm
import sys

#Scenario: module file and the code files are in different directories
import sys
sys.path.append('Users/Rida/Dev Projects/my_module.py')
#After this, set path variables using Nano in terminal

#----Standard Libraries----
import random
courses = ['Maths', 'Urdu', 'Physics','CompSci']
random_course = random.choice(courses)
print(random_course)

import math 
rads = math.radians(90)
print(rads)

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2024))

import os
print(os.getcwd()) #shows current directory
print(os.__file__) #view location of a module using dunder file __

import antigravity
