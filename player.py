def game_help():
    print('\nTo play, the current player needs to input a valid move and hit enter.\nValid moves should be 2 '
          'characters long. These characters will determine where you symbol (X or O) is placed.\nThe first '
          'character will determine which row you want to place your symbol ("t" to top row, "m" for middle row, '
          'and "b" for bottom row).\nThe second character will determine which column you want to place your '
          'symbol ("r" for right column, "m" for middle column, and "l" for left column).\nFor example: If you '
          'wanted to place your symbol in the top right corner, you would enter "tr" and hit enter.\nYou cannot '
          'place your symbol in a space that is already occupied.\n')


class Player:

    # Creates player and assigns corresponding number and symbol
    def __init__(self, num):
        self.num = num
        if num == 1:
            self.symbol = 'X'
        else:
            self.symbol = 'O'

    # Prompts current player for input and checks if input is a valid move
    def player_move(self, board, current_p):
        text_to_num = {'t': 0, 'm': 1, 'b': 2, 'l': 0, 'r': 2}
        move_is_valid = False
        while not move_is_valid:
            player_input = input(f'Player {self.num} please select a move: ').lower()
            if player_input == 'help':
                game_help()
                continue
            # Input should be exactly 2 characters
            elif len(player_input) != 2:
                print('Move is not valid! Input should be 2 characters')
                continue
            # Input should have t, m, or b as the first character, and l, m, r as the second character
            try:
                move = [text_to_num[player_input[0]], text_to_num[player_input[1]]]
                if board.update_board(move, current_p.symbol):
                    move_is_valid = True
            except KeyError:
                print('Move is not valid!')

    # Switches current player to the other player
    def switch_player(self, p1, p2):
        if self.num == 1:
            return p2
        else:
            return p1
