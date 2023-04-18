import random
from settings import *
from exceptions import *


class Enemy:
    level = 0

    def __init__(self):
        self.level = INITIAL_ENEMY_LEVEL
        self.health = self.level

    def decrease_health(self):
        try:
            self.health -= 1
            if self.health < 1:
                raise EnemyDown
        except EnemyDown:
            self.level += 1
            player.score += SCORE_ENEMY_DOWN

    def select_attack(self):
        self.attack = random.choice(['1', '2', '3'])
        return self.attack

    def select_defence(self):
        return random.choice(['1', '2', '3'])


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.health = INITIAL_PLAYER_HEALS

    def decrease_health(self):
        try:
            self.health -= 1
            if self.health < 1:
                raise GameOver
        except GameOver:
            pass

    def select_defence(self):
        self.defence = input(f'Choose your hero to defence: \n 1 - Wizard, 2 - Thief, 3 - Knight: ')
        return self.defence

    def select_attack(self):
        self.attack = input(f'Choose your hero to attack: \n 1 - Wizard, 2 - Thief, 3 - Knight: ')
        return self.attack


player = Player("sasha")
enemy = Enemy()


def draw():
    result = "IT'S A DRAW!"
    return result


def victory_attack():
    enemy.decrease_health()
    player.score += 1
    return f'YOUR ATTACK IS SUCCESSFUL!'


def fail_attack():
    player.decrease_health()
    return f'YOUR ATTACK IS FAILED!'


def victory_def():
    enemy.decrease_health()
    player.score += 1
    return f'YOUR DEFENCE IS SUCCESSFUL!'


def fail_def():
    player.decrease_health()
    return f'YOUR DEFENCE IS FAILED!'


def play_attack():
    choice = player.select_attack()
    computer_choice = enemy.select_defence()
    if choice == computer_choice:
        print(draw())

    elif choice == '1':
        if computer_choice == '3':
            print(victory_attack())
        elif computer_choice == '2':
            print(fail_attack())

    elif choice == '2':
        if computer_choice == '1':
            print(victory_attack())
        elif computer_choice == '3':
            print(fail_attack())

    elif choice == '3':
        if computer_choice == '2':
            print(victory_attack())
        elif computer_choice == '1':
            print(fail_attack())
    else:
        print('Try another number')
    print('------------------------------------')


def play_def():
    choice = player.select_defence()
    computer_choice = enemy.select_attack()
    if choice == computer_choice:
        print(draw())

    elif choice == '1':
        if computer_choice == '3':
            print(victory_def())
        elif computer_choice == '2':
            print(fail_def())

    elif choice == '2':
        if computer_choice == '1':
            print(victory_def())
        elif computer_choice == '3':
            print(fail_def())

    elif choice == '3':
        if computer_choice == '2':
            print(victory_def())
        elif computer_choice == '1':
            print(fail_def())
    else:
        print('Try another number')
    print('------------------------------------')
