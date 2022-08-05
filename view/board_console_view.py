from view.board_view import BoardView
from model.game import Board

class BoardConsoleView(BoardView):

    SYMBOLS = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, board: Board):
        super().__init__(board)

    def display_board(self):
        print('\n  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')
        print('--+---+---+---+---+---+---+---+---+')
        for row in enumerate(self.board.mat, 1):
            print(f' {row[0]}|', end='')
            for cell in row[1]:
                print(f' {self.SYMBOLS[cell.color_obj.value]} |', end='')
            print('\n--+---+---+---+---+---+---+---+---+')
        