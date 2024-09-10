# 1. Write a program to print your name.
# Method 1 - 

# Name = "Prashant Kokande"
# print("My name is " + Name)



# Method 2 -
# Name = "Prashant Kokande"

# def name():
    # for char in Name:
       # print(char)
#name()



#Method 3 -
#My_name = "Prashant_kokande"  # Your input string
#Display_name = []  # Initialize an empty list

#for i in My_name:  # Loop through each character in the string
#    Display_name.append(i)  # Append each character to the list

#print(Display_name)  # Print the final list

#Method 4 -
#My_name = input("Enter Your Name")
#print(f"Your name is {My_name}")

#---------------------------------------------------------------------------------------------------------------------------------#

# 2. Write a program for a Single line comment and multi-line comments
# This is single line comment
#print("Above line is single line comment")

#""" 
#This is multiline comment.
#"""
#print("Above line is multiline comment")

#---------------------------------------------------------------------------------------------------------------------------------#
'''
# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
# Integer Value
A = int (123)
print(A)
print(type(A))

# String Value
B = str("Prashant Kokande")
print(B)
print(type(B))

# Float Value
C = float(1.0)
print(C)
print(type(C))

#Boolean value
D = True
print(D)
print(type(D))

#Double 
E = 5.14657823
# Double (In Python, float itself is a double-precision floating-point number)
print(E)
print(type(E))

'''
#---------------------------------------------------------------------------------------------------------------------------------#

# 4. Define the local and Global variables with the same name and print both variables andunderstand the scope of the variables
# Global Variable
x = 10

def local_variable_fun():
    x = 20 #local variable
    print("This is local variable", x)

local_variable_fun()
print("This is global variable", x)


