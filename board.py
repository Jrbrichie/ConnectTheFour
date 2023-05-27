class Board:
    board = [[" " for col in range(6)] for row in range(7)]

    """
    print_board() prints the board in the proper format
    since the lists within the board are actually columns in the game,
    the printing of rows and columns are reversed to suit the Connect the Four token-placing mechanic
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
    valid_column(col) takes in a column argument where the player wants to place their token
    a column is valid if the column is not full, the column does not exceed 6 or is not less than 1
    and if the column is an integer.
    :returns true if position is valid 
    """
    def valid_column(self, col):
        valid_col = False
        column_nums = ["1", "2", "3", "4", "5", "6", "7"]

        # checks the string version of col is a string version of a column
        if col in column_nums:
            col = int(col)
            valid_col = not self.board[col - 1][5] != " "  # is true when the column is not full

        return valid_col


    """
	place_token(token, col) takes in the player's token and the column where the player wants to place their token
	it pushes a token into the next available column given that the column is not empty
	:returns true if token placement is successful, else it returns false
	"""
    def place_token(self, token, col):
        for i in range(len(self.board[col])):
            if self.board[col][i] == " ":
                self.board[col][i] = token
                break


    """
	is_board_full() checks if all positions in the board have been filled
	:returns true if board is full
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
	vertical_win(token) takes in a token argument that belonging to the player
	it checks if that player has 4 tokens vertically, 
	:returns true if there are four tokens on top of each other 
	"""
    def vertical_win(self, token):
        for i in range(0, 7):
            for j in range(0, 3):
                win = True

                # goes through each adjacent vertical position next to current to see if it is the same as the token
                for k in range(0, 4):
                    if token != self.board[i][j + k]:
                        win = False
                        break

                # if all 4 are the same, then the method returns true
                if win:
                    return True

                #
                # # this checks the first and fourth adjacent vertical tokens needed for a vertical win
                # # it removes the need for a loop which is less efficient considering it needs to loop through all 4 tokens
                # if b[i][j] == b[i][j + 3]:
                #     if b[i][j] == b[i][j + 1] and b[i][j] == b[i][j + 2]:
                #         return True

        return False


    """
	horizontal_win(token) takes in a token argument that belonging to the player
	it checks if that player has 4 tokens horizontally, 
	:returns true if there are four tokens next to each other 
	"""
    def horizontal_win(self, token):
        # goes through first 4 columns and all rows of the visible board (NOT THE ACTUAL 2D ARRAY BOARD)
        for i in range(0, 4):
            for j in range(0, 6):
                win = True

                # goes through each adjacent horizontal position next to current to see if it is the same as the token
                for k in range(0, 4):
                    if token != self.board[i + k][j]:
                        win = False
                        break

                # if all 4 are the same, then the method returns true
                if win:
                    return True

        return False

    """
	diagonal_right_win() checks if that player has 4 tokens vertically, 
	it returns the token if they have four tokens diagonally to the right
	"""
    def diagonal_right_win(self):
        pass

    """
	diagonal_left_win() checks if that player has 4 tokens vertically, 
	it returns the token if they have four tokens diagonally to the left 
	"""
    def diagonal_left_win(self):
        pass

    """
	player_win takes in a player token variable and checks all win conditions
	:returns true if any of the win conditions are met 
	"""
    def player_win(self, token):
        return self.vertical_win(token) or self.horizontal_win(token)
