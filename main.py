from random import choice

CHOICES = ['left', 'right']


def main():
    print('''
You enter the Tomb of King Ramses in search of the ancient tome that
will reverse the curse that is ravaging the island. After traversing the various
hallways, killing monsters and avoiding traps, you come to a fork in hallway.
Choose a path and let the fates decide.
''')

    player = input('Go \'left\' or \'right\': ')
    hallway = choice(CHOICES)

    if player == hallway:
        print(f'''
You continue down the {hallway} hallway. Eventually, you end up in an underground
chapel with two statues of King Ramses. As you enter, the statues eyes light up
and the mouths open up, revealing a button in each. One of the buttons leads
to the treasure room which has the ancient tome. Chhose a button and let the
fates decide.
''')

        player = input('Press the \'left\' or \'right\': ')
        button = choice(CHOICES)

        if player == button:
            print(f'''
You press the {button} button. The statues slide open to reveal a hidden chamber.
The ancient tome sits on the pedestal. You take the tome but now you must
fight your way out of the Tomb. TO BE CONTINUED...
''')
        else:
            print('''
The entrance shuts behind you and the statues laugh as a
mysterious gas enters the chamber. You realize that this
gas is poisonous. You struggle to breath and eventually
pass out and die. GAME OVER!
''')
    else:
        print('''
You continue down the path but you trip over rock and accidently set off trap. The floor opens up under you, revealing a spike pit. You fall to your death. GAME OVER!
''')


if __name__ == '__main__':
    main()
