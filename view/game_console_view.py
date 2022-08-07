from model.board import Board
from model.game import ReversiGame
from model.player import Player
from view.game_view import GameView
from view.board_console_view import BoardConsoleView


class GameConsoleView(GameView):
    ""
    def __init__(self, game: ReversiGame, board_size=8) -> None:
        super().__init__(game, board_size)            


    def pass_board_to_board_cons_view(self):
        self.board_view = BoardConsoleView(self.game.board)


    def display_welcome_meessage(self):
        print("\nWelcome to Reversi!")
        print("===================")
    

    def get_board_size(self):
        ""
        while True:
            board_size = input('Please enter the desired board size (even integer): ')
            try:
                board_size = int(board_size)
            except ValueError:
                print('Given value is not an integer.')
                continue

            if board_size % 2 != 0:
                print('Given integer is not an even number.')
                continue

            return board_size


    def display_score(self, players_list: list):
        ""
        print('\n*****Scores*****')
        for player in players_list:
            print(f'Player {(player.color_name).title()}: {player.score}')
        print('')


    def get_move(self, player: Player, board):
        """ Gets move from the user. Only task done here is user input 
        and formatting into a tuple of the kind (int, int), regardless
        of the nr of digits each int has.
        """
        while True:
            users_move_raw = input(f'Player {(player.color_name).title()}, '
            'please enter the "x,y" coordinates of your new disk: ')
            try:
                comma_index = users_move_raw.find(',')
            except:
                continue
            dig1 = users_move_raw[:comma_index]
            dig2 = users_move_raw[comma_index + 1:]
            try:
                if int(dig1) and int(dig2):
                    users_move = (int(dig1), int(dig2))
                    return users_move
            except ValueError:
                continue


    def display_board(self):
        self.board_view.display_board()        


    def display_winner(self, player_winner: Player, player_loser: Player):
        print(f'\nWinner is {player_winner} with a score of {player_winner.score}.'
        f'\nLoser is {player_loser} with a score of {player_loser.score}.')

