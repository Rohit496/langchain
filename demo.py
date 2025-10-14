import modules

result = modules.sum(5, 10)
print(result)
print(modules.diff(10, 5))


# with as
import modules as mathutils

print(mathutils.sum(5, 10))
print(mathutils.diff(10, 5))

# with from
from modules import sum, diff

print(sum(5, 10))
print(diff(10, 5))

# using *
from modules import *

print(sum(5, 10))
print(diff(10, 5))
