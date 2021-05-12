# ----------------------------------------------------------------------------------------
# Project: <Insert Project Name>
# Author: <Insert Name>
# Contributors: (i.e., these are people you worked on the code with)
#    - ...
# References: (i.e., nothing formal, simply a link to your source and a brief explanation
#    - ...
# ----------------------------------------------------------------------------------------
# ^This is good practice to provide either a "signature" and your sources or a README file

print("What is Object-Oriented Programming?")
print("It is a method of structuring a program by bundling related properties and behaviours into individual objects.")

print("These are the OOP Principles:")
print("Encapsulation (data hiding, data mining), Abstraction, Inheritance, and Polymorphism")
print("To data hide, simply put '__' before your variable name such as:")
print("     __variableName = <insert value>")
print("Encapsulation - What the client sees and what the programmer sees are "
      "different" + "\n" + "Abstraction - How the client thinks the program is run versus how it is actually run")
# For the above print statement I used concatenation - str + str + str + ...

# comments
print("Comments are signified with a '#' and are used to explain certain line(s) of code.")
print('Doc strings are signified with """ and are used to explain functions/methods.')

# example of using a doc string
def foo():
    """
    This is a function that prints '123'
    """
    print('123')
# to call this function: (We will learn more about functions next class)
foo()

# variable
print("Python has an identifier that POINTS to a variable name. This variable name REFERENCES/STORES a value(s).")
variableName = 123  # variableName is referencing to the value 123
# <variableName> = <value>

# re-declaring variables
B = 'ABC'
# re-declare B to 123 instead like so:
B = 123

print("Caching is the same as declaring or re-declaring variables. However, they differ in their purpose. Caching is "
      "used to optimize a program's run time.")
print("Think: If I want to know how many books are in the library, do I store (i.e., cache) "
      "the value and update it whenever I need to, or do I count all the books in the library every time I need to "
      "update how many books there are? You would probable cache this value.")

# aliasing
C = 123
D = 'ABC'
# I want D to be an alias for C
D = C  # D is an alias of C
# Try printing D and C now using print(). They should both now print 123 (since they both point to the same value).

E = 123  # Is E the same as C? They have the same values but are they the same in memory? Try printing the id for C
# and E: print(id())

print("Mutable - can change the value directly")
print("Immutable - requires reassigning the changed value to a new variable")

# str methods: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
print("String (str) is a sequence of characters within single or double quotation marks. (Immutable)")
# previous explained concatenation
# you could make a string using ',' like: print("A", "B", "C")
# join() is better explained in the link I provided

# int methods: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
print("Integers are whole numbers. (Immutable)")

# float methods: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
print("Floats are numbers with a decimal point. (Immutable)")

# Is '123.4' a float or a str? Is 123.0 a float or an int? Think on this.

# To test boolean values:
# print(1 == 1)
# print(A > B)  # you can assess that 2 > 1 but also that A > B
# Feel free to play around with this
print("Boolean values print True or False values (True corresponds with 1 and False corresponds with 0).")

print("Complex numbers are used mostly with lambda functions. They are real numbers mixed with imaginary numbers.")
y = lambda x: 10*x + 4  # referred by: y = mx + b
# now I'll call this lambda function (the imaginary part is x while the real part is 10 and 4)
print(y(12))  # now I passed in 12 as the argument for x in the lambda function (it computes the answer)

# list methods: https://www.w3schools.com/python/python_ref_list.asp
print("This is a list: A = [] and you fill it with values that can be separated by commas like: A = [1, 2, 3] "
      "(Mutable, Ordered, Duplicates)")
aList = [1, 2, 3]
# Try to get the index of 0 and now try to get an index of 3 (Why do you get an error?)
# index by: <Name of Container>[index]

# tuple methods: https://www.w3schools.com/python/python_ref_tuple.asp
print("This is a tuple: A = () and you fill it with values that can be separated by commas like: A = (1, 2, 3) "
      "(Immutable, Ordered, Duplicates)")
aTuple = (1, 2, 3)
# Try to get the index of 1

print("Iteration is pretty much an idea of going through a cycle. So, if I have three iteractions, this means 3 "
      "cycles.")
print("range(start, stop, step):", " start - inclusion and "
                                   "usually starts at 0", " stop - exclusion and is the lenbth of the container",
      " step - how many increments you'd like to do")
# Try these out:
for i in range(0, 4):  # range(0, 4) is equivalent to range(4), try range(1, 4) or range(1, 3)
    print(i)  # what would happen if you increment by 2? range(0, 4, 2)

# set methods: https://www.w3schools.com/python/python_ref_set.asp
print("This is a set - A = {} and you fill it like so: A = {1, 2, 3} (Mutable, Unordered, No duplicates)")
aSet = {1, 2, 3}
# Try printing this set three times print()

# dictionary methods: https://www.w3schools.com/python/python_ref_dictionary.asp
print("This is a dictionary - A = {} and you fill it like so: A = {'A': 1, 'B': 2, 'C': 3} (Unordered)")
print("Dictionaries are indexed by keys which have to be unique and immutable.")
print("Dictionary values can be anything you want. Allows duplicate values.")
aDict = {'A': 1, 'B': 2, 'C': 3}
# Try indexing the 'B' and printing its value

# How to debug: pick a breakpoint, instead of run choose debug and watch the console and debugger
# resume program = lets you skip iterations
# step over = steps over the line
# step in = steps into the line
# Try debugging this:
n = 0  # initially 0
for i in range(4):
    n += 1
print(n)
# I suggest playing around with this

# And that's all we learned! Happy learning, everyone.
