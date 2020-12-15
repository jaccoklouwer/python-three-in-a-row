class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = None
        self.winner = None
        self.board = self.set_board()

    @staticmethod
    def set_board():
        return [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def check_win(self, player):
        for row in range(len(self.board) - 1):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] == player.symbol:
                return True
            if self.board[0][row] == self.board[1][row] == self.board[2][row] and self.board[0][row] == player.symbol:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] == player.symbol:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] == player.symbol:
            return True
        return False

    def print_board(self):
        for row in range(len(self.board)):
            print('|\t', end='')
            for cel in range(len(self.board[row])):
                if self.board[row][cel] == self.player1.symbol:
                    print(self.player1.symbol + '\t|\t', end='')
                elif self.board[row][cel] == self.player2.symbol:
                    print(self.player2.symbol + '\t|\t', end='')
                else:
                    print('\t|\t', end='')
            print()

    def play(self):
        self.current_player = self.player1

        draw = False
        steps = 9
        while self.winner is None or draw:
            self.current_player.play_set(self.board)

            self.print_board()

            if self.check_win(self.current_player):
                self.winner = self.current_player

            steps = steps - 1
            print('there are ' + str(steps) + ' moves left')
            print()

            if steps == 0:
                break

            self.switch_players()

            if self.winner is not None:
                print('The winner is: ' + self.winner.name)
            if draw:
                print('it\'s a Draw.')

    def switch_players(self):
        if self.current_player is self.player1:
            self.current_player = self.player2
        elif self.current_player is self.player2:
            self.current_player = self.player1
