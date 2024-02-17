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
    def update_board(self, move, symbol):
        if self.board[move[0]][move[1]] == ' ':
            self.board[move[0]][move[1]] = symbol
            return True
        else:
            print('Move is not valid! Space is already taken.')
            return False

    # Checks board for winner or if there are no more empty spaces
    def check_board(self, p_num):
        if self.is_winner(p_num) or self.is_full():
            if self.is_full() and not self.is_winner(p_num):
                print('Draw!')
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
    def is_winner(self, p_num):
        winner_text = f'Player {p_num} is the winner!'
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
