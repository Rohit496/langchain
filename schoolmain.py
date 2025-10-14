# main.py

from school import *  # Import all public names from the package

add_student("Rohit")
add_teacher("Anjali")

# These will NOT work because they are not in __all__
# remove_student("Rohit")
# remove_teacher("Anjali")
