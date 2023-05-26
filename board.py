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

    """
	placeToken takes in a token variable and the column where the player wants to place their token
	it pushes a token into the next available column given that the column is not empty
	returns true if token placement is successful, else it returns false
	"""

    def place_token(self, p, col):

        if not self.is_col_full(col):
            self.board[col].append(p)  # pushes the token into the desired column
            return True

        else:
            return False

    # is_col_full checks if the column is full, if full it returns true
    def is_col_full(self, col):
        return self.board[col][6] != " "

    """
	full checks if all positions in the board have been filled
	if full it returns true
	"""

    def full(self):
        is_full = False

        for i in range(7):
            for j in range(6):
                if self.board[i][j] == " ":
                    is_full = True
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