import random
print('Hello and welcome to the guessing game!')

val = random.randint(0, 100)
print('val: ' + str(val))

print('The objective of the game is to guess what number I am thinking of.')

def calculate():
    print('Please type your guess.')
    guess = int(input())
    if guess < val:
        print('Too low! try again')
        calculate()

    elif guess > val:
        print('Too high! try again')
        calculate()

    elif guess == val:
        print('That is correct, you win!')

calculate()
