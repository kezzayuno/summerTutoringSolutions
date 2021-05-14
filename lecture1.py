# # str formatting
# print("The Orangutan loves the coconut.")  # less flexible compared to...
# animal = 'Dog'
# food = 'chicken'
# print("The %s loves the %s." % (animal, food))
# # What if I want to change the animal?
# print()
# # More concrete example...
# for i in range(3):
#     print('The number is: {:^05}'.format(i))  # the placeholder allows change to a certain argument
# # What if we want to make a float point with a certain amount of digits after the decimal point? {.2f}
# # What about pre-fillers? 05 Left-skew <, right-skew >? Width 5?
# print()
# for i in range(3):  # this is equivalent
#     print('The number is: %d' % (i))
# # Center skew? Must go to format() ^ or use str.center(<width>)


# # for loops
# dict1 = {'A': 1, 'B': 2, 'C': 3}
# list1 = ['A', 'B', 'C']
# for i in dict1.values(): # what about .keys() and .values()
#     print(i, end='')  # removes the new line (\n)
# print('\n')
# for i in list1:  # prints the items themselves
#     print(i)
# print()
# for i in range(len(list1)):  # prints their index
#     print(i)
# print()
# for i in range(len(list1)):
#     print(list1[i])  # using index number to get the item in the container
# # nested for loops
# for i in range(3):  # How would you use this to make a grid? If this is a grid: [] and there are rows [[], [], []]
#     for n in range(2):
#         y = 1 + 1  # this doesn't do anything, what is important to see is the nest for loop nature


# # while loops
# flag = True  # initially true
# n = 3
# i = 0
# while flag:  # What if I put just True
#     i += 1
#     if i == n:
#         flag = False  # condition that "turns off" the loop
#         # What would happen if I didn't have this flag?
#         # using continue and break instead of a flag


# # functions
# def foo():
#     for i in range(3):
#         return 1 + 1
#
# def foo2():
#     yield 1 + 1
#     yield 1 + 2
#     yield 1 + 3
#
# def main():  # think of main() as what makes the calls
#     foo()  # this is a call (doesn't catch the result); use print()
#     x = lambda a,b: a + b + 5
#     print(x(5, 6))
#     y = foo2()
#     for i in y:  # makes a function() iterable
#         print(i)
#     print(y)  # does not print the like an iterable container such as a list
#     # print(next(y))  # What happens when I simply call next(y) after the for loop
#
# main()


# # boolean
# A = True  # what if A was False instead
# B = True  # what if both are false
# if A:
#     print('Nice job.')
# elif B:
#     print('Amazing job.')
# else:
#     print('Woops.')
# print()
# # compared to:
# if A:
#     print("Nice job.")
# if B:
#     print('Amazing job.')
# if not B and not A:
#     print('Woops.')


# side effect: is it mutable or not?
A = [1, 2, 3]
print(A)
def foo3(A):
    A.append(4)  # no return statement and no assigned variable catch the result and yet...
foo3(A)
print(A)
B = '123'
print(B)
def foo4(B):
    B + '4'
B = foo4(B)
print(B)
