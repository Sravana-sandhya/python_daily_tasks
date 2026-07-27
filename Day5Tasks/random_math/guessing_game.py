# Q4 : Create a Number Guessing Game where: 
#● The program generates a random number between 1 and 50 using random. 
#● The user has 5 attempts to guess the number. 
#● After each guess, calculate the absolute difference using math.fabs() and display how far the guess is from the correct number.
import random
import math
random_number = random.randint(1,50)
for i in range(1,6):
    guess = int(input("Enter your guess :"))
    if guess == random_number:
        print("you guessed the correct number.")
        break
    else:
        difference = math.fabs(random_number - guess)
        print("Wrong guess")
        print("yao are", difference,"away from the number.")
else:
    print("Game over")