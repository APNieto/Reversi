from model.board import Board
from model.game import ReversiGame
from model.player import Player
from model.game_rules import GameRules
from view.game_view import GameView
from view.board_console_view import BoardConsoleView


class GameConsoleView(GameView):
    ""
    def __init__(self, game: ReversiGame, board_size=8) -> None:
        super().__init__(game, board_size)    
        self.board_view = BoardConsoleView(game.board)

    def display_welcome_meessage(self):
        print("\nWelcome to Reversi!")
        print("===================")

    def display_score(self, players_list: list):
        ""
        print('\n*****Scores*****')
        for player in players_list:
            print(f'Player {(player.color_name).title()}: {player.score}')
        print('')



    def get_move(self, player: Player, board):
        """Gets an position input from the current player in the
        string format (x,y) for his next move. The function takes
        care of format and rules validation by means of helper 
        functions. Input is limited to one-digit sizes for each
        coordinate.
        Args:
            player (Player): Player object, with its distinguishing color_name attribute.
        Returns:
            self.users_move: tuple with (x,y) coordinates
        """
        while True:
            self.users_move_raw = input(f'Player {(player.color_name).title()}, '
            'please enter the "x,y" coordinates of your new disk: ')
            self.format_validated_move = self.validate_format(self.users_move_raw)         
            if GameRules.exist_convertible_disks(player, self.format_validated_move, board):    # If there exist points to be converted for the given user point,
                return self.format_validated_move                                               # then return the user's point as validated.
                
    def validate_move(self, player, position, board):
        """ Helper function """        
        GameRules.is_valid_move(player, position, board)
        if GameRules.end_points_for_conversion:
            return True
        else:
            print('The new position must be within the board size '
            f'{self.board_size}x{self.board_size} and must have disks '
            'of the opposite availble for conversion in its sorroundings.')
            return False      
          
    def validate_format(self, position):
        """ Helper function """
        error_input_text = 'The pair of coordinates must be in the format "x,y" ("" not needed): '
        is_input_correct = False
        while not is_input_correct:
            if len(position) == 3 and position[1] == ',':
                try:
                    format_validated_move = tuple((int(position[0]), int(position[2])))
                    is_input_correct = True
                except ValueError:
                    position = input(error_input_text)
            else:
                position = input(error_input_text)          
        return format_validated_move



    def display_board(self):
        self.board_view.display_board()        

    def display_winner(self, player_winner: Player, player_loser: Player):
        print(f'\nWinner is {player_winner} with a score of {player_winner.score}.'
        f'\nLoser is {player_loser} with a score of {player_loser.score}.')

