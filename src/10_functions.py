# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(x):
    if x % 2 == 0:
        print(True)
    else:
        print(False)

print('Number is 6:')
is_even(6)
print('Number is 7:')
is_even(7)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if num % 2 == 0:
    print("Even!")
else:
    print("Odd")

