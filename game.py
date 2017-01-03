# Put your code here
import random

print "Greetings!"
name = raw_input("Please introduce yourself: ")
print name, "Let's play a game!"
print name, "I'm thinking of a number between 1 and 100... wanna guess?"
solution = random.randint(0, 100)


def guessing():
    still_guessing = True
    num_guesses = 0
    while still_guessing:
        user_guess = int(raw_input("Please enter your guess: "))
        num_guesses += 1
        if user_guess > solution:
            print "your guess is too high.  Try again."
        elif user_guess < solution:
            print "your guess is too low. Try again"
        else:
            print "Yay, you are correct!"
            print "It took you only %i guesses" % num_guesses
            still_guessing = False

guessing()
