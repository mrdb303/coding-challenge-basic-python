# Coding Challenge Level 2 - Find the max and min of a Python Set
#
# Print the max and min numbers of this set
# set([15, 11, 8, 15, 32, 20])
# For example 8 and 32


example_set = ([15, 11, 8, 15, 32, 20])


# Approach 1 - Using the built-in functions:

print("\nBuilt-in functions:")
print("The maximum number in the set is " + str(max(example_set)) + ".")
print("The minimum number in the set is " + str(min(example_set)) + ".")


# Approach 2 - Creating and using custom functions:

def get_max(data_set):
    maximum = data_set[0]

    for element in data_set:
        if element > maximum:
            maximum = element
	
    return maximum


def get_min(data_set):
    minimum = data_set[0]

    for element in data_set:
        if element < minimum:
            minimum = element
	
    return minimum


print("\nCustom functions:")
print("The maximum number in the set is " + str(get_max(example_set)) + ".")
print("The minimum number in the set is " + str(get_min(example_set)) + ".")