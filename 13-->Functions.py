# A function is a block of code which only runs when it is called.
# So basically, a function is a set of commands that are followed when they are asked to (called). It helps in stopping repititive coding.


# Addition using function in python

def add(a,b):
    return a+b
    
s = int(input('Enter first number: '))
t = int(input("Enter second number: "))
print(add(s,t))



# Greeting using function

def greet(name = 'Stranger'):
    print("Good day, " + name)

a = input("Enter your name: ")
greet(a)
greet("Harsh")
greet() #default parameter value is set to 'Stranger'
