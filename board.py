class Board:
    board = [[" " for col in range(6)] for row in range(7)]

    """
    print_board() prints the board in the proper format
    since the lists within the board are actually columns in the game,
    the printing of rows and columns are reversed
    """
    def print_board(self):
        print("+---+---+---+---+---+---+---+")
        for i in range(5, -1, -1):
            row = ""

            for j in range(7):
                row += self.board[j][i] + " | "  # prints the column then row
            print("| " + row[:-2] + "|")
            print("+---+---+---+---+---+---+---+")

        print("  1   2   3   4   5   6   7 ")


    """
    valid_column(col) takes in a column argument that the user inputs.
    a column is valid if the column is not full, the column does not exceed 6 or is not less than 1
    and if the column is an integer.
    :returns true if position is valid 
    """
    def valid_column(self, col):
        valid_col = False
        columns = ["1", "2", "3", "4", "5", "6", "7"]

        if col in columns:
            col = int(col)
            valid_col = 7 > col >= 0 and not self.is_col_full(col)

        return valid_col


    """
	place_token takes in a token variable and the column where the player wants to place their token
	it pushes a token into the next available column given that the column is not empty
	returns true if token placement is successful, else it returns false
	"""
    def place_token(self, token, col):
        for i in range(len(self.board[col])):
            if self.board[col][i] == " ":
                self.board[col][i] = token
                break

    """
    is_col_full takes in a col argument that the user inputs
    :returns true if the column still has space, false if it is full 
    """
    def is_col_full(self, col):
        return self.board[col][5] != " "

    """
	is_board_full checks if all positions in the board have been filled
	if full it returns true
	"""
    def is_board_full(self):
        is_full = True

        for i in range(7):
            for j in range(6):
                if self.board[i][j] == " ":
                    is_full = False
                    break
            else:  # only executes if the inner "j" loop is not broken (breaks out of the outerloop)
                continue
            break

        return is_full

    """
	vertical_win checks if that player has 4 tokens vertically, 
	it returns the token if they have four tokens on top of each other 
	"""

    def vertical_win(self):
        pass

    """
	horizontal_win checks if that player has 4 tokens horizontally, 
	it returns the token if they have four tokens next to each other 
	"""

    def horizontal_win(self):
        pass

    """
	diagonal_right_win checks if that player has 4 tokens vertically, 
	it returns the token if they have four tokens diagonally to the right
	"""

    def diagonal_right_win(self):
        pass

    """
	diagonal_left_win checks if that player has 4 tokens vertically, 
	it returns the token if they have four tokens diagonally to the left 
	"""

    def diagonal_left_win(self):
        pass

    """
	player_win takes in a player token variable and checks all win conditions
	"""

    def player_win(self, p):
        pass