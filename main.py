# Imports
import board
import player

board = board.Board()
player1 = player.Player(1)
player2 = player.Player(2)
current_player = player1
game_is_active = True

# Game will run until there is a winner or until no more moves can be made
while game_is_active:
    board.show_board()
    current_player.player_move(board, current_player)
    if board.check_board(current_player.num):
        board.show_board()
        print('Game Over!')
        game_is_active = False
    current_player = current_player.switch_player(player1, player2)
