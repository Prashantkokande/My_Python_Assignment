# 1. Write a program to print “Bright IT Career” ten times using for loop
'''
name = "Bright IT Career"
for i in range(10):
    print(name)

'''  
#---------------------------------------------------------------------------------------------------------------------------------#
# 2. Write a java program to print 1 to 20 numbers using the while loop.
# Python progam using the while loop
'''
num = 1
while num <= 20:
    print(num)
    num += 1
'''  
#---------------------------------------------------------------------------------------------------------------------------------#
# 3. Program to equal operator and not equal operators
'''
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

if num1 == num2:
    print (f"{num1} == {num2}: {num1 == num2}")
else:
    print(f"{num1} != {num2}: {num1 != num2}")
'''

#---------------------------------------------------------------------------------------------------------------------------------#
# 4. Write a program to print the odd and even numbers.
'''
value = int(input("Enter your number "))

def evenodd():
    if value%2 == 0:
        print("Given number is even: ")
    else:
        print("Given number is odd: ")
evenodd()

'''
# another way
'''
value1 = int(input("Enter range of starting number "))
value2 = int(input("Enter range of ending number "))

if value1 > value2:
    print("Starting number must be less than or equal to ending number.")
else:
    def even_odd_numbers(start, end):
        print("Even numbers:")
        for i in range(start, end + 1):
            if i % 2 == 0:
                print(i, end=" ")
        
        print("\nOdd numbers:")
        for i in range(start, end + 1):
            if i % 2 != 0:
                print(i, end=" ")

    even_odd_numbers(value1, value2)
'''  
#---------------------------------------------------------------------------------------------------------------------------------#
# 5. Write a program to print largest number among three numbers.
'''
def find_largest(a,b,c):
     return max(a,b,c)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

x = find_largest(a,b,c)
print(f'The largest number is {x}:')
'''
# another way using if else statement
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b & a > c:
    print (f"{a} is the largest number")
elif b > a & b > c:
    print (f"{b} is the largest number")    
else:
    print(f"{c} is the largest number")
'''

#---------------------------------------------------------------------------------------------------------------------------------#
# 6. Write a program to print even number between 10 and 20 using while
'''
a = 10
b = 20
print("Even Numbers Between 10 to 20: ",end=" ")
while a <= b:
    if(a % 2 == 0):
        print("{0}".format(a),end=" ")
    a = a + 1
print()
'''

#---------------------------------------------------------------------------------------------------------------------------------#
# 7. Write a program to print 1 to 10 using the do-while loop statement.
'''
i = 1

while True:  
    print(i)
    i += 1
    
    if i > 10:  
        break
'''

#---------------------------------------------------------------------------------------------------------------------------------#
# 8. Write a program to find Armstrong number or not
'''
a = int(input('Enter a number '))
sum = 0
temp = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if a == sum:
    print(a," is an amstrong number")
else:
    print(a," is not an amstrong number")
'''

#---------------------------------------------------------------------------------------------------------------------------------#
#9. Write a program to find the prime or not.
'''
number = int(input("Enter any number to check prime number or not: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")

'''

#---------------------------------------------------------------------------------------------------------------------------------#
# 10. Write a program to palindrome or not.
'''
n = int(input("Enter number to check palindrome or not:"))
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if(temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!") 
'''

#---------------------------------------------------------------------------------------------------------------------------------#
# 11. Program to check whether a number is EVEN or ODD using switch
# Python program don't have switch inbuilt function 

#---------------------------------------------------------------------------------------------------------------------------------#
# 12. Print gender (Male/Female) program according to given M/F using switch
# Python program don't have switch inbuilt function, we can write this program using if else statement.
'''
gender = input("Enter your gender ")
if gender not in ['M', 'F', 'm', 'f']:
    print("Given input is not correct")
else:
    if gender in ['M', 'm']:
        print("Your gender is Male")
    else:
        print("Your gender is Female")
'''