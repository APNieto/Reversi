from view.board_view import BoardView
from model.game import Board


class BoardConsoleView(BoardView):

    SYMBOLS = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, board: Board):
        super().__init__(board)

    def display_board(self):        
        print('\n  |', end='')  # Print header row with nrs
        for s in range(self.board.size):
            if len(str(s + 1)) == 1:
                print(f' {s + 1} |', end='')
            else:
                print(f' {s + 1}|', end='')
        print('\n--+', end='')  # Print 1st separator
        for s in range(self.board.size):
            print('---+', end='')
        print('')
        for row in enumerate(self.board.mat, 1):  # Print row of disk colors
            if len(str(row[0])) == 1:
                print(f' {row[0]}|', end='')
            else:
                print(f'{row[0]}|', end='')
            for cell in row[1]:
                print(f' {self.SYMBOLS[cell.color_obj.value]} |', end='')
            print('\n--+', end='')   # Print separator
            for s in range(self.board.size):
                print('---+', end='')
            print('')
        