# 10.Packages
# 1. Create a program to create two class.
# 1.1. Create a constructor and a method for each class
# 1.2. Create a __init__.py for adding all packages
# 1.3. Import the respective packages
# 1.4. Call each class by creating an object to it
# 1.5. Create a program by all the above

# Importing classes from the package
# One folder "my_package" created for packages, importing from there. Pls refer that
from my_package.class_one import ClassOne
from my_package.class_two import ClassTwo

# Create an instance of ClassOne
obj1 = ClassOne("Prashant")
obj1.greet()  

# Create an instance of ClassTwo
obj2 = ClassTwo(29)
obj2.show_age()  # Output: ClassTwo: The age is 29.
