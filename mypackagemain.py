# main.py

# Import the package
import my_package

# Use functions from the package
print(my_package.add(10, 5))
print(my_package.subtract(8, 3))
print(my_package.to_upper("salesforce"))
print(my_package.to_lower("SALESFORCE"))

# specific imports
from my_package.math_utils import add, subtract
from my_package.string_utils import to_lower, to_upper

print(add(20, 30))
print(subtract(50, 25))
print(to_lower("PYTHON PROGRAMMING"))
print(to_upper("python programming"))

# using alias
from my_package.string_utils import to_upper as uppercase

print(uppercase("hello world"))


# using wildcard import
from my_package.math_utils import *

print(add(100, 200))
print(subtract(500, 300))
