# Coding Challenge: Level 1 - Find the duplicates in a Python Tuple
#
# How many times is 1 duplicated in the following Tuple?
# 1,1,2,3,4,1,5,6,7,1
#
# For example 1 is in the Tuple 4 times


supplied_tuple = (1,1,2,3,4,1,5,6,7,1)
look_for = 1

# Approach 1 - Using the built-in function:

print(str(look_for) + " is in the tuple " + str(supplied_tuple.count(look_for))\
    + " time(s).")


# Approach 2 - Creating and using a custom function:

def find_instances_of(value, tuple_data):
    instances = 0

    for element in range(len(tuple_data)):
        if value == tuple_data[element]:
            instances += 1

    return instances


instances_found = find_instances_of(look_for, supplied_tuple)
print(str(look_for) + " is in the tuple " + str(instances_found) + " time(s).")

