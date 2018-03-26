"""
From the Talk Python Training.
Competed 2017-12-29
"""
import random

print('----------------------------------------')
print('---------GUESS THAT NUMBER GAME---------')
print('----------------------------------------')
print('')

that_number = random.randint(0,100)
name = 'anon'
guess = -1
guess_count = 0
name = input('Player, what is your name? ')

while guess != that_number:
    guess_text = input('Guess a number from 0 to 100: ')
    guess = int(guess_text)
    guess_count += 1
    if guess < that_number:
        print('Sorry {}, Your guess of {} is too low.'.format(name, guess))
    elif guess > that_number:
        print('Sorry {1},Your guess of {0} is too high.'.format(guess, name))
    elif guess == that_number:
        print('You got it in {} tries.'.format(guess_count))
    else:
        print('ERROR')
print('done')
