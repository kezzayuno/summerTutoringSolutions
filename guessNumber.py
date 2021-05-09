# should have random imported
import random


def chooseNumber():
    # generating the number in the range 1-100
    rand_num = random.randint(1, 100)

    return rand_num


def main():
    win = False
    guessAmount = 10
    n = 0

    # call and receive the generated num
    rand_num = chooseNumber()

    # should continue to prompt until they guess correctly
    while not win and n != guessAmount:

        user_guess = input("Guess a number between 1-100: ")
        print()

        # should check for valid type
        if user_guess.isdigit():

            user_guess = int(user_guess)

            # should check that the int is within range
            if 1 <= user_guess <= 100:

                # should compare the nums and print the appropriate messages
                if user_guess == rand_num:
                    print("Congratulations! The number you guessed was", user_guess, "and the number generated was",
                          rand_num, '!')
                    print("Thank you for playing...Goodbye!")
                    # makes sure to exit the program
                    win = True
                else:
                    print("Sorry!", user_guess, "is not the number.")
                    if int(user_guess) > rand_num:
                        print('You guessed too high.', end=' ')
                    else:
                        print('You guessed too low.', end=' ')
                    print("Try again\n")
                    n += 1
            else:
                # warning message
                print(user_guess, "is out of range\n")
        else:
            # warning message
            print("'" + user_guess + "' is not a valid number\n")
    if not win:
        print("Unfortunately you ran out of guesses. You lose. Goodbye!")


main()