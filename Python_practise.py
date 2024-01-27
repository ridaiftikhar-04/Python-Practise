#practise
#Functions

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