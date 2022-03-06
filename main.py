import random
import sympy as sympy

name = input('Write you name here: ')


def Start():
    print(
        f'Hello {name.capitalize()}! Would you like to play a game? If you can guess what number i am thinking off i will give you a surprise!')
    print('First hint: Its between 1-200')


def Hints():
    global hints, number
    hints = []
    number = random.randint(1, 200)
    if number % 2 == 0:
        hints.append('The number i am thinking of is even.')
    else:
        hints.append('The number i am thinking of is odd.')

    if number % 3 == 0:
        hints.append('The number i am thinking of is evenly dividable with 3.')
    else:
        hints.append('The number i am thinking of is not evenly dividable with 3.')

    if number % 5 == 0:
        hints.append('The number i am thinking of is evenly dividable with 5.')
    else:
        hints.append('The number i am thinking of is not evenly dividable with 5.')

    if sympy.isprime(number):
        hints.append('The number i am thinking of is a prime number.')
    else:
        hints.append('The number i am thinking of is not a prime number.')

    if number <= 100:
        hints.append('The number i am thinking of is less or equals than 100.')
    else:
        hints.append('The number i am thinking of is bigger than 100.')

    return hints, number


Start()
Hints()
while True:
    global hints, number
    guess = input('Guess a number: ')
    if guess.isnumeric():
        guess = round(float(guess), 1)
        if guess > 200:
            print('You guess a number higher than 200..')
            continue
    else:
        print(f'You did not write a number. {guess}')
        continue


    if int(guess) == number:
        print('You won. You guess my numbers. Your prize will be: nothing... Sorry!')
        break
    else:
        if len(hints) > 0:
            hint = random.choice(hints)
            hints.pop(hints.index(hint))
            print(hint)
        else:

            if number < int(guess):
                print(f'The number i am thinking of is lower than {int(guess)}')
            else:
                print(f'The number i am thinking of is higher than {int(guess)}')

