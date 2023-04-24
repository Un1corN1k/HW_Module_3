import random
import settings
import exceptions


class Enemy:

    def __init__(self, level=settings.INITIAL_ENEMY_LEVEL):
        self.level = level
        self.health = level

    def decrease_health(self):
        self.health -= 1
        if self.health < 1:
            raise exceptions.EnemyDown

    def select_attack(self):
        return random.choice(settings.VALID_CHOICES)

    def select_defence(self):
        return random.choice(settings.VALID_CHOICES)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.health = settings.INITIAL_PLAYER_HEALS

    def decrease_health(self):
        self.health -= 1
        if self.health < 1:
            raise exceptions.GameOver

    @staticmethod
    def _select_choice():
        choice = None
        while choice not in settings.VALID_CHOICES:
            try:
                choice = int(input("Choose your hero to attack: \n 1 - Wizard, 2 - Thief, 3 - Knight: "))
            except ValueError:
                pass

        return choice

    def select_defence(self):
        return self._select_choice()

    def select_attack(self):
        return self._select_choice()

    def attack(self, enemy):
        attack = self.select_attack()
        defence = enemy.select_defence()
        fight_result = fight(attack, defence)

        if fight_result == FightResult.SUCCESS:
            try:
                enemy.decrease_health()
                self.score += settings.SCORE_SUCCESS_ATTACK
            except exceptions.EnemyDown:
                self.score += settings.SCORE_ENEMY_DOWN
                raise
            finally:
                print(settings.SUCCESSFUL_ATTACK)

        elif fight_result == FightResult.FAIL:
            print(settings.FAILED_ATTACK)

        elif fight_result == FightResult.DRAW:
            print(settings.DRAW)

        print('------------------------------------')

    def defence(self, enemy):
        defence = self.select_defence()
        attack = enemy.select_attack()
        fight_result = fight(attack, defence)

        if fight_result == FightResult.SUCCESS:
            print(settings.FAILED_DEFENCE)
            self.decrease_health()

        elif fight_result == FightResult.FAIL:
            print(settings.SUCCESSFUL_DEFENCE)

        elif fight_result == FightResult.DRAW:
            print(settings.DRAW)

        print('------------------------------------')


class FightResult:

    SUCCESS = 1
    FAIL = -1
    DRAW = 0


def fight(attack, defence):
    if attack == defence:
        return FightResult.DRAW

    if (attack, defence) in settings.SUCCESSFUL_ATTACKS:
        return FightResult.SUCCESS
    return FightResult.FAIL
