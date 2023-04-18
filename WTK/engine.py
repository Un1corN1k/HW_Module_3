from models import *


def get_player_name():
    return input("Hello, please enter your name to start the game: ")


def play():
    name = get_player_name()
    print(f"Welcome {name}, have a good luck!")
    while player.health >= 1:
        play_attack()
        play_def()
    print(f"{name}, you lose.\nYou defeat Boss level {enemy.level}, and have {player.score} score!")

play()
