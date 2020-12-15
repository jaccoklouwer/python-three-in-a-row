from Game import Game
from player import Player


def play():
    player_1_name = ''
    player_2_name = ''
    player1 = None
    player2 = None

    while player_1_name == '' or player_2_name == '' or player_1_name == player_2_name:
        player_1_name = input("Player 1, what is your name: ")
        player_2_name = input('Player 2, What is your name: ')
        player1 = Player(player_1_name, 'X')
        player2 = Player(player_2_name, 'O')

    game = Game(player1, player2)
    game.play()


if __name__ == '__main__':
    play()
