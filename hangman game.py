import time

name = input("What is your name?")  # welcoming the user
print("Hello, " + name + ", Time to play hangman!")

print(" ")

time.sleep(1)  # wait for 1 second

print("Start guessing...")

time.sleep(0.5)

# Set the secret word and print a hint
secret_word = "engineering"
print("\nHint: This is a large, gray animal.")

guesses = ""  # creates an variable with an empty value
correct_guesses = ""  # store correctly guessed letters

turns = 10  # determine the number of turns

# Create a while loop
while turns > 0:  # check if the turns are more than zero
    failed = 0  # make a counter that starts with zero

    for char in secret_word:  # for every character in secret_word
        if char in guesses:
            if char in correct_guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:  # print You Won
        print("\nYou've cracked the code!")  # print You Won
        break  # exit the script

    print()

    guess = input("Guess a character: ")  # ask the user go guess a character
    guesses += guess  # set the players guess to guesses

    if guess in secret_word:
        correct_guesses += guess  # add correctly guessed letter

    if guess not in secret_word:  # if the guess is not found in the secret word
        turns -= 1  # turns counter decreases with 1 (now 9)
        print("\nOops, that's not quite right.")  # print wrong
        print("You have", turns, "more guesses")  # how many turns are left

    if turns == 0:  # if the turns are equal to zero
        print("\nUh-oh, you've run out of tries!")  # print "You Lose"
        print("The word was:", secret_word)