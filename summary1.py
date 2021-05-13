# str formatting
# Write this in str formatting (format() or C formatting):
# Hello, I was wondering if 000Jess000 got the same answer as I did for Question 3? I got 1.45.
# Make sure to use the right formats (i.e., if it's a float, use #f or #.#f

# Using str formatting (either format() or C formatting) draw this:
# ^^^----^^^
# 0        0
#     o
#    ---
# vvv----vvv
#     |
#     |
#     |
#     |
# ----  ----
#  |      |
# Hint: Look at the picture line by line

# Here is the solution:
# print("{:^^10}".format("----"))
# print("{0:<5}{0:>5}".format(0))
# print("{:^10}".format('o'))
# print("{:^10}".format('---'))
# print("{:v^10}".format("----"))
# print("{0:^10}\n{0:^10}\n{0:^10}\n{0:^10}".format('|'))
# print("{0:<5}{0:>5}".format('----'))
# print(" {0:<4}{0:>4}".format('|'))

# for loop
# Create a dictionary using strings: A, B, and C with their corresponding values: 1, 2, 3
# Create a three different for loops that iterate over its items(), keys(), and values()
# Create a list and iterate the items in this list and print() them
# Using the same list, iterate and print() the item indexes
# Using the same list, iterate over every other item (e.g., if it was [1, 2, 3, 4], it would print: [1, 3] (skips 2, 4)

# debug this nested for loop to see for yourself how a nested for loop works
for i in range(3):
    print(' i', end='')
    for n in range(3):
        print(' n', end='')
        for k in range(3):
            print(' k', end='')
# printed the iterations to show you the general pattern of a nested for loop

# while loop
# while loop requires to have a flag to "turn off" the while loop
flag = True  # initially True
m = 0  # initially zero
while flag:
    print("Flag hasn't turned off the while loop")
    m += 1
    if m == 3:
        flag = False  # flag turns off when the body of the while loop has done its job
        # the "job" in this case is for m == 3
# Replace the flag with a break to see what break is like
# Try: If m == 3, break, else: continue

# if else statements
print("These are the main compound booleans: and, or, not (also called negation)")
# Create the follow if else statements:
# First, I'll give you an example
# if 1 equals 2 and 4 is greater than 2, print("True"), else: print("False")
# if 1 == 2 and 4 > 2:
#     print("True")
# else:
#     print("False")
# What do you think this will print?
# Try replacing the == with is

# Try it yourself:
# If 12 == 7 or 12 == 24 - 12, print True
# You have x = 12. If lambda with the variable x with the complex number x**2 equal 144, print True
# If you eat supper and do not yell or remain quiet, you will get dessert. (Assume supper and yell are variables)
# See how these are equivalent: If you eat supper, you will get dessert. If you will not eat supper, then no dessert.
#   First is a "positive" version while the latter is the negation but they're essentially doing the same thing

# Solution for the harder ones:
# if lambda x: x**2 == 144:
#     print("That is true, yes.")
# if supper and (not yell or quiet):
#     print("Dessert")

A = True
B = False

# Which will print?
if A and B:
    print('Wow.')
elif not A and not B:
    print("Hmmm.")
elif not A and B:
    print("That's something.")
else:
    print("Ya got me.")

# Why are the outputs for these if statements different despite having the same conditions?
print()  # Empty print statements make space (look at the output to see this effect)
if A:
    print("A")
if B:
    print("B")
if not B:
    print("not B")
print()
if A:
    print("A")
elif B:
    print("B")
elif not B:
    print("not B")
print()
# Try to make a nested if else statement to get familiar with these

# Think about how you would use complex booleans with a while loop...
# Remember that the order of the compound boolean may matter due to Lazy Evaluation (keep this in mind)

# functions
# Create a main() and make sure to call it
# Create a function that adds its parameter int m by 1
#   Call this function in main() and print this function's result in main()
#   Do you need a return statement here? Why do you think that is or isn't the case?
#   If you were not going to use a return statement, how would you display the result?
# Create a lambda function for Pythagoras Theorem
#    print the result of lambda using whatever numbers you'd like
# Use debugger to see for yourself how a generator functions works:
def generatorFunction(m):
    yield 2 + m
    yield 2 + m
    yield 2 + m

def generatorFunction1(n):  # I provided this to show you a for loop in a generator function
    for i in range (3):
        yield n + 1

m = 0
for n in generatorFunction(m):
    m = n
    print(m)  # What do you think this will print? Was it what you expected?
# Note: for generator functions, you can yield it for as long as you'd like through the whole program

g = 0
for e in range(3):
    print(next(generatorFunction(g)))  # this is another way to call a generator function

# Try debugging this:
def foo(m):
    return foo2(m + 3)

def foo2(n):
    return n + 3

def main():
    print(foo(3))

main()

# solutions:
# def foo(m):
#     return m + 1
#
# def main():
#     number = foo(1)
#     print(number)
#     y = lambda a,b: (a**2 + b**2)*(1/2)
#     print(y(2, 2))
#
# main()

# Side Effects will indefinitely be encountered while you're doing your projects! Watch out for them.
