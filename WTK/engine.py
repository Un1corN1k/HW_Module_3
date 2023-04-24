from models import Player, Enemy
from exceptions import EnemyDown, GameOver


def get_player_name():
    name = ""
    while not name:
        name = input("Hello, please enter your name to start the game: ").strip()
    return name


def play():
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy()

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            enemy = Enemy(enemy.level + 1)
        except GameOver:
            with open("score.txt", 'w+') as score:
                score.write(f'{player.name}\t{player.score}')
            print(f"Game over!\n{player.name}, you have {player.score} points,\n"
                  f"Boss level {enemy.level} beat you!")
            break


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        pass
