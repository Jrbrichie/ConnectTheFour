class Board:
    board = [[" " for col in range(6)] for row in range(7)]


    def print_board(self):
        print("+---+---+---+---+---+---+---+")
        for i in range(5, -1, -1):
            row = ""
            for j in range(7):
                row += self.board[j][i] + " | "
            print("| " + row[:-2] + "|")
            print("+---+---+---+---+---+---+---+")

        print("  1   2   3   4   5   6   7 ")

    """
    valid_position(pos) takes in a position argument that the user inputs
    a position is valid if the column is not full and the position does not exceed 6 or is not less than 1
    returns true if position is valid 
    """
    def valid_position(self, pos):
        return 7 > pos >= 0 and not self.is_col_full(pos)

    """
	place_token takes in a token variable and the column where the player wants to place their token
	it pushes a token into the next available column given that the column is not empty
	returns true if token placement is successful, else it returns false
	"""
    def place_token(self, token, col):
        self.board[col].append(token)  # pushes the token into the desired column

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