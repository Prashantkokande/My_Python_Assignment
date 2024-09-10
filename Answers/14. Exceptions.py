# 1. Write a program to generate Arithmetic Exception without exception handling
'''
result = 0
def arithmetic_program(a, b):
    result = a + b
    return result
result = arithmetic_program(10,10)
print(result)
'''
# ---------------------------------------------------------------------------------------------------------------------
# 2. Handle the Arithmetic exception using try-catch block
'''
result = 0
def arithmetic_program(a, b):
    try:
        result = a + b
        return result
    except Exception as e:
        print("An error occurred:", e)
        return None

result = arithmetic_program(10, 10)
print(result)
'''
#----------------------------------------------------------------------------------------------------------------------
# 3. Write a method which throws exception, Call that method in main class without try block
'''
class ArithmeticOperation:
    def throw_exception(self):
        raise Exception("Custom exception from throw_exception method")

if __name__ == "__main__":
    
    operation = ArithmeticOperation()
    operation.throw_exception()  
    print("This line will not execute because of the exception.")
'''
#----------------------------------------------------------------------------------------------------------------------
# 4. Write a program with multiple catch blocks
# 5. Write a program to throw exception with your own message

'''
def arithmetic_program(data):
    try:
        number = int(data)
        print("Converted number:", number)

        result = number + 'text'
        print("Result:", result)

    except ValueError as e:
        print("Caught ValueError: Invalid literal for int() with base 10 -", e)  # Own message

    except TypeError as e:
        print("Caught TypeError: Unsupported operation -", e)   # Own message

    except Exception as e:
        print("Caught a generic exception:", e)    # Own message

arithmetic_program("123")  
arithmetic_program("abc")  
'''
#----------------------------------------------------------------------------------------------------------------------
# 6. Write a program to create your own exception
'''
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_value(value):
    if value < 0:
        raise MyException("Negative values are not allowed!")

try:
    check_value(-5)
except MyException as e:
    print("Caught MyException:", e)
'''
#----------------------------------------------------------------------------------------------------------------------
#7. Write a program with finally block
'''
def list_operations():
    try:
        my_list = [1, 2, 3, 4, 5]

        print("Element at index 2:", my_list[2])

        print("Element at index 10:", my_list[10])
    
    except IndexError as e:
        print("Caught IndexError:", e)
    
    finally:
        print("This is finally block ")

list_operations()
'''
#----------------------------------------------------------------------------------------------------------------------
# 9. Write a program to generate FileNotFoundException
'''
def generate_file_not_found_error(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:", content)
    
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)

generate_file_not_found_error('non_existent_file.txt')
'''

#----------------------------------------------------------------------------------------------------------------------
# 10. Write a program to generate ClassNotFoundException
'''
def class_not_found():
    try:
        import prashant

        var = prashant.kokande_class()
    
    except ImportError as e:
        print("ClassNotFoundException :", e)
class_not_found()
'''

#----------------------------------------------------------------------------------------------------------------------
# 11. Write a program to generate IOException
'''
import os
def generate_io_exception():
    try:
        with open('/file.txt', 'w') as file:
            file.write("Attempting to write to a protected file.")
    
    except OSError as e:
        print("Generated IOException :", e)

generate_io_exception()
'''
#----------------------------------------------------------------------------------------------------------------------
# 12. Write a program to generate NoSuchFieldException

class ExampleClass:
    def __init__(self):
        self.existing_field = "This field exists"

def generate_no_such_field_exception():
    obj = ExampleClass()
    
    try:
        non_existent_field = obj.non_existent_field
    except AttributeError as e:
        print("NoSuchFieldException :", e)

# Call the function
generate_no_such_field_exception()

