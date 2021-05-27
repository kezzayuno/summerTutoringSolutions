choice = input("Would you like to play? (Y/N): > ")
while choice not in ['y', 'Y', 'n', 'N']:
    choice = input("Sorry, that is an invalid request.\nWould you like to play? (Y/N): > ")
givenPoints = []

while choice.lower() == 'y':
    x = int(input("What is the x coordinate of your point: > "))
    y = int(input("What is the y coordinate of your point: > "))
    if not (x, y) in givenPoints:
        givenPoints.append((x, y))
        # they can assume that what is given is a integer
        if x == 0 and y == 0:  # origin
            print("Your given point is located at the origin.")
        elif x > 0 and y > 0:  # y and x is in positive quadrant
            print("Your given point is located at Quadrant II.")
        elif x < 0 and y < 0:  # y and x is in the negative quadrant
            print("Your given point is located at Quadrant III.")
        else:
            if x < 0:  # x is negative, y is positive
                print("Your given point is located at Quadrant I.")
            else:  # x is positive, y is negative
                print("You given point is located at Quadrant IV.")
    else:
        print("This given point is already stored.")

    choice = input("Do you still want to input points? (Y/N): > ")

if givenPoints and choice.lower() == 'n':
    x = int(input("Which x point would you like to use: > "))
    y = int(input("Which y point would you like to use: > "))
    if (x, y) in givenPoints:
        distance = (x**2 + y**2)**(1/2)
        print("The distance between ({}, {}) and the origin (0, 0): {:.2f}".format(x, y, distance))
    else:
        print('This point does not exist.')

print("Thank you for playing. Goodbye...")