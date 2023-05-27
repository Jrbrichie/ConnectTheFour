import board


class Game:
    b = board.Board()
    p1 = "X"
    p2 = "O"

    """
	turn(option) takes in the option for who goes first
	it uses recursion that keeps asking the player to choose who goes first until either p1/p2 is inputted
	"""
    def turn(self, option):

        p1_turn = False

        if option == "p1":
            p1_turn = True
        elif option != "p2" and option != "p1":

            # calls the turn(option) function again to check if the new input is valid
            new_p1_turn = self.turn(input(option + " is not an option! Please enter a valid option: "))
            p1_turn = new_p1_turn

        return p1_turn

    """
    win_message(p1_turn) takes in the p1_turn determining whose turn it was when the game was won
    it prints the win message with the appropriate player
    """
    def win_message(self, p1_turn):
        player = "2"
        if p1_turn:
            player = "1"

        print("")
        self.b.print_board()
        print("\nPlayer " + player + " has won Connect the Four! Congratulations!!!")

    """
	game_loop(p1_turn) takes p1_turn to determine which player goes first
	continues running until a player wins OR the board is full
	"""
    def game_loop(self, p1_turn):
        player_won = False

        # continues running as long as the board is not full
        while not self.b.is_board_full():
            self.b.print_board()

            # determines the message and token for the player currently playing
            if p1_turn:
                p_text = "Player 1"
                p_token = self.p1
            else:
                p_text = "Player 2"
                p_token = self.p2

            if p1_turn:
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
            if self.b.player_win(p_token):
                player_won = True
                break

            p1_turn = not p1_turn  # gives the other player their turn

        # if a player wins, a win message is outputted,
        if player_won:
            self.win_message(p1_turn)
        # otherwise it outputs that the board is full and asks if they want to play again
        else:
            # TODO create board full and play again mechanics
            print("Board is full! Play again? (y/n): ")

    """
    play() asks the user for who goes first
    also, it runs game_loop which starts the actual game 
    """
    def play(self):
        print("Welcome to Connect the Four!\nPlayer 1 is X\nPlayer 2 is O\n")
        p1_first = self.turn(input("Who goes first? (p1/p2): "))

        self.game_loop(p1_first)


g = Game()
g.play()
