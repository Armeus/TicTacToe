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
            # Input should be exactly 2 characters
            if len(player_input) != 2:
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
