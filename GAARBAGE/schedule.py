#make a random day
#check if fits
# must have 3 on and 6 on eg, and rest on pioneer

#have x amount of slots in a day
# fill the slots and check if it works

import random

# Sample list of employees
employees = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivan", "Julia", "Kevin", "Luna", "Mike"]

# Shuffle the list to randomize the order
random.shuffle(employees)

# Assign 3 employees to the first office
first_office = employees[:3]

# Assign 6 different employees to the second office
second_office = employees[3:9]

# Assign the remaining employees to the main office
main_office = employees[9:]

# Display the assignments
print(first_office, second_office, main_office)

