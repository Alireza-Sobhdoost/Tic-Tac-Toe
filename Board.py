from colorama import Fore , Style
from copy import deepcopy

class Board:
    def __init__(self, board=None):
        # define players
        self.player_1 = 'x'
        self.player_2 = 'o'
        self.empty_square = '.'
        self.position = {}
        self.init_board()


        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)


    def init_board(self):

        for row in range(3):
            for col in range(3):
                self.position[row, col] = self.empty_square

    def __str__(self):
        # define board string representation
        board_string = ''

        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                board_string += ' %s' % self.position[row, col]

            # print new line every row
            board_string += '\n'

        # prepend side to move

        # return board string
        return board_string

    def make_move(self, coord):

        board = Board(self)
        if (coord[0] > 2 or coord[0] < 0) or (coord[1] > 2 or coord[1] < 0) or (board.position[coord[0] , coord[1]] != board.empty_square) :
            print(Fore.RED + 'Invalid coordinate' + Style.RESET_ALL)
            return None
        # Correct assignment based on the value of turn (assuming turn indicates 'x' or 'o')

        board.position[coord[0] , coord[1]] = self.player_1

            # swap players
        (board.player_1, board.player_2) = (board.player_2, board.player_1)

            # return new board state
        return board

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.position[i, 0] == self.position[i, 1] == self.position[i, 2] != '.':
                return self.position[i, 0]
            if self.position[0, i] == self.position[1, i] == self.position[2, i] != '.':
                return self.position[0, i]

        if self.position[0, 0] == self.position[1, 1] == self.position[2, 2] != '.':
            return self.position[0, 0]
        if self.position[0, 2] == self.position[1, 1] == self.position[2, 0] != '.':
            return self.position[0, 2]

        return None

    def check_draw(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.position[i, j] == '.':
                    count += 1
        return count

    def generate_states(self):
        # define states list (move list - list of available actions to consider)
        actions = []
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # make sure that current square is empty
                if self.position[row, col] == self.empty_square:
                    # append available action/board state to action list
                    actions.append(self.make_move([row, col]))

        # return the list of available actions (board class instances)
        return actions
# Create an instance of Board
b1 = Board()  # Instantiate the Board class
result = b1.make_move([2, 2])  # Change (2, 2) to 'x' since turn is 0
