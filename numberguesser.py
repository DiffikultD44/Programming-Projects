#guess numbers
import random as r

number = r.randint(1, 100)
guess_amount = 0


while True:
    guess = int(input("guess a number from 1 to 100 >>>"))
    
    guess_amount += 1
    if guess > number:
        print("the number is smaller than %d" %guess)

    if guess < number:
        print("number is greater than %d" %guess)
    if guess == number:
        break
print("correct! the number was %d, it took you %d guesses" %(number, guess_amount))