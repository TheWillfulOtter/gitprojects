#  wizard game


import random
import time

from wizards_actors import Wizard, Creature, SmallAnimal, Dragon, BadWizard

def main():
    print_header()
    game_loop()

def print_header():
     print('----------------------------------------')
     print('-------------- Wizard Game -------------')
     print('----------------------------------------')
     print('')


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        SmallAnimal('Bat', 3),
        Creature('Tiger', 12),
        Dragon('Dragon', 50, 75, True),
        Wizard('Sauran', 100),
        Creature('Brad', 10),
        ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of {} has appeard from a dark a foggy forest...'
            .format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]unaway. or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The Wizard {} runs and hides, taking time to recover...".format(hero.name))
                time.sleep(4)
                print("The Wizard {} returns rested.".format(hero.name))
        elif cmd == 'r':
            print('The once mighty Wizard {} has become unsure of his surroundings and flees.')
        elif cmd == 'l':
            print('The Wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('You must choose a, r, or l.  You died.')
            break

        if not creatures:
                print("You've defeted all the creatures!")
                break
        print()

if __name__ =='__main__':
    main()
