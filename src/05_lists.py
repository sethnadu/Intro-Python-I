# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
print(x.append(4))
print("Problem 1:", x)


# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
print(x.extend(y))
print("Problem 2:", x)


# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
print(x.remove(8))
print("Problem 3:", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
print(x.insert(5, 99))
print("Problem 4:", x)

# Print the length of list x
# YOUR CODE HERE 
print("Length of list x", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
x_multiplied = [i * 1000 for i in x]
print("X list values * by 1000", x_multiplied)