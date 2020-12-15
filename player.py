class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def play_set(self, board):
        correct_input = False
        while correct_input is False:
            row = self.check_input_for('row')
            col = self.check_input_for('column')

            if row and col and board[row][col] == '':
                board[row][col] = self.symbol
                correct_input = True

    def check_input_for(self, input_value):
        try:
            number = int(input(self.name + ', on which ' + input_value + ' do you want to set your symbol: ')) - 1
        except ValueError:
            print('The input is not a number between 1 and 3')
            return False

        if 1 <= number <= 3 and number != '':
            return number
        else:
            print('it needs to be a number between 1 and 3')
            return False
