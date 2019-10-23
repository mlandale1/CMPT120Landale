# CMPT 120 Intro to Programming
# Lab #6 - Lists and Error Handling
# Author: Matt Landale
# Created: 2019-10-21
import random

def board_display(board):
   print('''   |   |  
 {} | {} | {}
   |   |
-----------
   |   |
 {} | {} | {} 
   |   |
-----------
   |   |
 {} | {} | {}
   |   |'''.format(*board[1:10]))
    


def player_move():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        letter = input('Player 1, Choose O or X to start the game: ').upper()
    if letter == 'X':
        return {'Player 1': 'X', 'Player 2': 'O'}
    else:
        return {'Player 2': 'X', 'Player 1': 'O'}

def first_move(players):
    random_player = 'Player {}'.format(random.randint(1, 2))
    return random_player, players[random_player]


def choice(board):
    while True:
        try:
            position = int(input("Choose a number 1-9: "))
            if position in range(1, 10) and board[position] == " ":
                return position
        except ValueError:
            pass

def tictactoe():
    board = [' ' for _ in range(10)]
    players = player_move()
    name, player_marker = first_move(players)
    print('{} with marker {} will go first.'.format(name, player_marker))
    while True:
        position = choice(board)
        board[position] = player_marker
        board_display(board)
        name = 'Player 1' if name == 'Player 2' else 'Player 2'
        player_marker = players[name]
        print(name, player_marker)
        
if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')
    while True:
        tictactoe()
    
        
        
