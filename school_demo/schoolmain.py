# main.py

import sys
import os

# Add the parent directory to sys.path to find the school module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from school import *  # Import all public names from the package

add_student("Rohit")
add_teacher("Anjali")

# These will NOT work because they are not in __all__
# remove_student("Rohit")
# remove_teacher("Anjali")
