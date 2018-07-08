# What is Time Tuple?
import time;  # This is required to include time module.
print(time.time()) #this gives us the time in seconds.

# Write a program to get formatted time.
import datetime #This is required to include module.
print(datetime.datetime.fromtimestamp(time.time()))

# Extract month from the time.
import datetime
a = '2018-06-22' #I really don't know dis is the corect way of doing dis...btt dis gives the output.
datee = datetime.datetime.strptime( a,"%Y-%m-%d")
print(datee.month)

#  Extract day from the time.
#import datetime
#from datetime import day
#print(day.today()

#  Write a program to print time using localtime method.
import datetime #This is required to include module.

now = datetime.datetime.now() #stores current date and time.
print("Current date and time using str method of datetime object:")
print(str(now))

#Find the factorial of a number input by user using math package functions.
num = int(input("Enter the no. : ")) #user enters number.
import math #This is required to include module.
# calculated factorial using factorial method.
print(math.factorial(num))

#  Find the GCD of a number input by user using math package functions.
#num1 = int(input("Enter the first no. : "))
#num2 = int(input("Enter the second no. : "))
#import math
#print("The GCD of numbers is :",math.gcd(num1,num2))

# Use OS package and do the following tasks:
# 1. Get current working directory.
# 2. Get the user environment.
import os #This is required to import the module.
print(os.getcwd())
print(os.name)