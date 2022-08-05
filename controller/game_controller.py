from model.game import ReversiGame
from model.game_rules import GameRules
from view.game_view import GameView

class GameController:

    def __init__(self, game: ReversiGame, view: GameView) -> None:
        self.game = game
        self.board = self.game.board
        self.view = view


    def run_game(self):
        
        self.view.display_welcome_meessage()
        has_winner = False
        while not has_winner:            
            
            #Display the board
            self.view.display_board()

            # Show score
            self.game.calculate_scores()
            self.view.display_score(self.game.players_list)

            # Ask current player for move and validate its format
            # If it is a valid move, then add the disk to the bord
            while True:  # TODO Generate different appropriate error messages for each type of invalid input, as with a dictionary, for example
                new_position = self.view.get_move(self.game.curr_player, self.board) 
                if GameRules.is_valid_move(self.game.curr_player, new_position, self.board):
                    self.board.add_disk(self.game.curr_player, new_position)
                    break
                else:
                    print(GameRules.error_codes[GameRules.last_error_code])                 
                       
            # Convert disks           
            self.board.convert_disks_in_all_dirs(new_position)

            # Check if winner

            # Change player
            self.game.change_player()