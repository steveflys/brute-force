import random
import string
guessAttempts = 0
myPassword = input("Enter a password for the computer to try and guess: ")
passwordLength = len(myPassword)
while True:
    guessAttempts = guessAttempts + 1
    passwordGuess = ''.join([random.choice(string.ascii_letters + string.digits)for n in range(passwordLength)])
    print(passwordGuess)
    if passwordGuess == myPassword:
        print("Password guessed successfully!")
        print("It took the computer %s guesses to guess your password." % (guessAttempts))
        break

