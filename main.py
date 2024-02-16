class Board:
    # Initializes empty board
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    # Prints board in current state
    def show_board(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if column < len(self.board[row]) - 1:
                    print(f' {self.board[row][column]} |', end='')
                else:
                    print(f' {self.board[row][column]} \n', end='')
            if row < len(self.board) - 1:
                print("-----------")

    # Updates board based on player move
    def update_board(self, move):
        if self.board[move[0]][move[1]] == ' ':
            self.board[move[0]][move[1]] = current_player.symbol
            return True
        else:
            print('Move is not valid! Space is already taken.')
            return False

    # Checks board for winner or if there are no more empty spaces
    def check_board(self):
        if self.is_winner() or self.is_full():
            return True
        else:
            return False

    # Checks if board is full (no more space for a valid move)
    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        print('There is no more space!')
        return True

    # Checks if there is a winner
    def is_winner(self):
        winner_text = (f'Player {current_player.num} is the winner!')
        # Checks for winning row
        for row in self.board:
            if row[0] == row[1] == row[2] and ' ' not in row:
                print(winner_text)
                return True
        # Checks for winning columns
        for i in range(3):
            column = [self.board[0][i], self.board[1][i], self.board[2][i]]
            if column[0] == column[1] == column[2] and ' ' not in column:
                print(winner_text)
                return True
        # Checks for diagonal win
        diagonal_down = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diagonal_up = [self.board[2][0], self.board[1][1], self.board[0][2]]
        if (diagonal_down[0] == diagonal_down[1] == diagonal_down[2] and ' ' not in diagonal_down) or (
                diagonal_up[0] == diagonal_up[1] == diagonal_up[2]) and ' ' not in diagonal_up:
            print(winner_text)
            return True

        # Returns False if no condition for a win is met
        return False


class Player:
    # Creates player and assigns corresponding number and symbol
    def __init__(self, num):
        self.num = num
        if num == 1:
            self.symbol = 'X'
        else:
            self.symbol = 'O'

    # Prompts current player for input and checks if input is a valid move
    def player_move(self):
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
                if board.update_board(move):
                    move_is_valid = True
            except KeyError:
                print('Move is not valid!')

    # Switches current player to the other player
    def switch_player(self):
        if self.num == 1:
            return player2
        else:
            return player1


board = Board()
player1 = Player(1)
player2 = Player(2)
current_player = player1
game_is_active = True

# Game will run until there is a winner or until no more moves can be made
while game_is_active:
    board.show_board()
    current_player.player_move()
    if board.check_board():
        board.show_board()
        print('Game Over!')
        game_is_active = False
    current_player = current_player.switch_player()
