# Put your code here
import random

print "Greetings!"
name = raw_input("Please introduce yourself: ")
print name, "Let's play a game!"
print name, "I'm thinking of a number between 1 and 100... wanna guess?"

score_list = []


def pick_number():
    solution = random.randint(1, 100)
    print "winning number is: %i" % solution
    return solution


def guessing(solution):
    still_guessing = True
    num_guesses = 0

    while still_guessing:
        user_guess = raw_input("Please enter your guess: ")
        num_guesses += 1
        try:
            user_guess = int(user_guess)
        except ValueError:
            print "That's not a number, %s! try again." % name
            continue
        if user_guess < 0 or user_guess > 100:
            print "Follow instructions stupid! Choose number between 1 and 100!"
        elif user_guess > solution:
            print "your guess is too high.  Try again."
        elif user_guess < solution:
            print "your guess is too low. Try again"
        else:
            print "Yay, you are correct!"
            print "It took you only %i guesses" % num_guesses
            score_list.append(num_guesses)
            replay = raw_input("Would you like to play again? y/n")
            if replay == "y":
                main()
            else:
                print "Thanks for playing!"
                still_guessing = False
                break
    print score_list
    print "Congrats! You best score was: ", min(score_list)


def main():
    solution = pick_number()
    guessing(solution)


if __name__ == '__main__':
    main()
