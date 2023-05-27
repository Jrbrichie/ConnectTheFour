import board


class Game:
    b = board.Board()
    p1 = "X"
    p2 = "O"

    """
	the recursive function turn() takes in the option for who goes first
	if it is p1, then it sets the p1_turn variable to true
	else if the option is not p2, then it calls the turn() function again with a new input 
	returns if player 1 goes first
	"""

    def turn(self, option):

        p1_turn = False

        if option == "p1":
            p1_turn = True
        elif option != "p2" and option != "p1":
            p1_turn = self.turn(input(option + " is not an option! Please enter a valid option: "))

        return p1_turn

    """
	win_message outputs the appropriate win message depending on who wins
	"""

    def win_message(self, p):
        pass

    """
	game_loop takes in the token characters of both players
	if continues running until a player wins OR the board is full
	"""

    def game_loop(self, p1_first):

        # continues running as long as the board is not full
        while not self.b.is_board_full():
            self.b.print_board()

            # determines the message and token for the player currently playing
            if p1_first:
                p_text = "Player 1"
                p_token = self.p1
            else:
                p_text = "Player 2"
                p_token = self.p2

            if p1_first:
                print("Player 1's turn!")
            else:
                print("Player 2's turn!")

            # asks the user to input a position on the board between 1-7 inclusive
            column = input(p_text + ", enter a position to put your token in (1-7): ")

            # continues running until the player inputs a valid int position on the board
            while not self.b.valid_column(column):
                new_column = input(str(column) + " is not a valid column! "
                                                 "Please enter a valid column (1-7): ")
                column = new_column

            column = int(column) - 1  # parsing the string into the int format

            self.b.place_token(p_token, column)  # places the current player's token in their desired column

            # TODO create and implement win conditions
            # self.b.player_win(p_token)

            p1_first = not p1_first

    """
    play() asks the user for who goes first
    also, it runs game_loop which starts the actual game 
    """

    def play(self):
        p1_first = self.turn(input("Who goes first? (p1/p2): "))

        self.game_loop(p1_first)


g = Game()
g.play()
