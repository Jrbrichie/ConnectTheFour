import board


class Game:
    b = board.Board()

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
        elif option != "p2":
            p1_turn = self.turn(input(option + "is not an option! Please enter a valid option: "))

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
    def game_loop(self, p1_first, p1, p2):

        while not self.b.full():
            self.b.print_board()

            # determines the message and token for the player currently playing
            if p1_first:
                p_text = "Player 1"
                p_token = p1
            else:
                p_text = "Player 2"
                p_token = p2

            position = -1
            while 7 < position < 0:
                position = int(input(p_text + ", enter a position to put your token in: "))

            self.b.place_token(p_token, position)
            self.b.player_win(p_token)

            p1_first = False

    """
    play() asks the user for two tokens representing the two players
    it user input for who goes first
    also, it runs game_loop which starts the actual game 
    """
    def play(self):
        # TODO add checkers for a valid token (?)
        p1 = input("Enter Player 1's Token: ")
        p2 = input("Enter Player 2's Token: ")

        p1_first = self.turn(input("Who goes first? (p1/p2): "))

        self.game_loop(p1_first, p1, p2)


g = Game()
g.b.print_board()
