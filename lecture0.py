# ----------------------------------------------------------------------------------------------------------------
# Assignment: Welcome to Python Basics
# Author: Kezziah Ayuno
# Contributors:
#    ...
# References:
#    ...
# ----------------------------------------------------------------------------------------------------------------

class Person:  # encapsulation, data hiding
    """
    Description: This is an example of base class called Person

    Methods:
        init()
        behaviours:
            CatchPhase()
        getter methods:
            GetName()
        setter methods:
            SetNewFav()

    Attributes:
        self.__name - Person instance's name
        self.favouriteFood - Person instance's favorite food
    """
    def __init__(self, name, food):
        """
        :param name: str of Person instance's name
        :param food: str of Person instance's favourite food
        """
        self.__name = name  # private
        self.favouriteFood = food  # public

    def CatchPhase(self):
        """
        Prints the Person's catch phase
        """
        print("{} said: Ain't that just the way!".format(self.__name))  # str formatting format()
        # print("%s said: Ain't that just the way!" % (self.__name)

    def GetName(self):
        """
        :return: name of the Person instance
        """
        return self.__name

    def SetNewFav(self, newFav):
        """
        Sets a new favorite food
        :param newFav: str of new favorite food
        """
        self.favouriteFood = newFav

class Student(Person):  # inheritance, polymorphism
    """
    Description: This is an example of a child class that inherits from Person class

    Methods:
        CatchPhase()

    Attributes: inherited from Parent class
    """
    def CatchPhase(self):
        """
        Overwrites Person class's catch phase to have a student specific phase
        """
        print("{} said: What did you get on Question 3?".format(self.GetName()))


KC = Person('Kezziah', 'Salmon')  # <variable> = <expression>
KC.CatchPhase()
print(KC.favouriteFood)
# print(KC.name)

Bryn = Student('Bryn', 'Chicken')  # uses the Person attributes = inheritance
Bryn.CatchPhase()

# Redefining Variables, hard coding
# integer  e.g., 123.0 would be a float
D = 123
# string
D = "123"  # or '123'
D = D + "456" + "789"  # concatenation
print(D)

# combining strings using ','
E = '123','456','789'
print(E)

# combining strings using .join()
F = 'ABC'.join(E)
print(F)

# No Aliasing:
G = []
H = []
print(G != H)  # bool, should be True because they have the same value
print(id(G))
print(id(H))
# Aliasing
B = 0
A = []
A = B
print(A == B)
# except Exception as e:
#   ...

# list
aList = [1, 2, 3]
print(aList[0])
# tuple
aTuple = (1, 2, 3)
print(aTuple[2])
# dictionary
aDict = {'A': 1, 'B': 2, 'C': 3}
print(aDict['B'])

# for debugging:
W = ['fizz', 'buzz', 'fizz', 'buzz']
n = 0
for i in range(4):
    n += 1
    W = W[:1]
print(W)
print(n)
