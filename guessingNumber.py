#import random package to generate a secrate number
import random
secretNumber=random.randint(1,10)
print('I am thinking of a number could you guess it between 1 and 10')
#Ask the player to guess the number 6 times
for guessesTaken in range(1,7):
    print('Take a guess')
    guess=int(input())
    if guess<secretNumber:
        print('Your guess is low')
    elif guess>secretNumber:
        print('Your guess is high')
    else:
        break #in this condition the player's guess is correct
if guess==secretNumber:
    print('Good job! You guessed my number in '+str(guessesTaken)+' guesses')
else:
    print('Better luck next time. The number is '+str(secretNumber))
