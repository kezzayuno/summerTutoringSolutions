import time
import random

file = open('poem.txt', 'r')
readFile = file.read()
print(readFile)
file.close()

file = open('poem.txt', 'r')
for line in file:
    print(line)
file.close()

file = open('poem.txt', 'r')
print(file.readline())
print(file.readline())
file.close()

file = open('poem.txt', 'r')
print(file.readlines())
# readFile = file.readlines()
# I want to remove the '\n' at the end, how do I do this? .strip('\n')
# cleanFile = []
# for line in readFile:
#     cleanFile.append(line.rstrip())
# print(cleanFile)
file.close()

# file = open('poem.txt', 'w')
# newText = file.write('Oh, man. What an amazing poem.')
# print(newText)  # Will this print the file? No.
# file.close()
# file = open('poem.txt', 'r')
# print(file.read())  # Notice how it overwrote the file
# file.close()

# file = open('poem.txt', 'a')
# newText = file.write('Oh, man. What an amazing poem.')  # Notice how we used write() but it serves a different purpose
# file.close()
# file = open('poem.txt', 'r')
# print(file.read())
# file.close()

# Good Practice (when opening a file):
with open('poem.txt') as f:
    readFile = f.read()
print(readFile)
# This automatically closes the file for you

# ASCII Table
chara = chr(97)
print(chara)
print(ord(chara))
# Notice how related these two functions are. These can be used for decrypting messages for example.

# file = open('times.txt', 'a')
# timeList = [time.perf_counter()]
# for i in range(100):
#     print(random.randint(0, 10))
#     timeList.append(time.perf_counter())
# for i in timeList:
#     file.write(str(i) + '\n')
# file.close()
#
# file = open('times2.txt', 'a')
# timeList = [time.perf_counter()]
# for i in range(100):
#     random.randint(0, 10)
#     for n in range(100):
#         random.randint(0, 10)
#         for j in range(100):
#             random.randint(0, 10)
#     timeList.append(time.perf_counter())
# for i in timeList:
#     file.write(str(i) + '\n')
# file.close()
# Can also make graphs using a very useful module: matplotlib: https://matplotlib.org/2.0.2/index.html

# Source: https://stackabuse.com/python-nested-functions/
# Nested functions
def function1(): # outer function
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()

function1()

def num1(x):
   def num2(y):
      return x * y
   return num2
res = num1(10)

print(res(5))

# Source: https://www.w3schools.com/python/ref_keyword_nonlocal.asp
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

c = 1 # global variable
def add():
    return c + 10

add()

# Source: https://www.programiz.com/python-programming/global-keyword
def foo():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar:", x)
    print("Calling bar now")
    bar()
    print("After calling bar:", x)


foo()
print("x in main:", x)

class Person():
    def foo6(self):
        print("I'm a thing.")

A = Person()
A.foo6()

del Person
# B = Person()
# This will delete the object class Person