# Imports
import board
import player

continue_play = True

while continue_play:
    new_board = board.Board()
    player1 = player.Player(1)
    player2 = player.Player(2)
    current_player = player1
    game_is_active = True

    # Game will run until there is a winner or until no more moves can be made
    while game_is_active:
        new_board.show_board()
        current_player.player_move(new_board, current_player)
        if new_board.check_board(current_player.num):
            new_board.show_board()
            print('Game Over!')
            game_is_active = False
        current_player = current_player.switch_player(player1, player2)

    answer = input('Would you like to play again? (y/n): ').lower()
    if answer == 'n':
        continue_play = False

print('Thank you for playing!')
