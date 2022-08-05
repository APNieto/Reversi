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

            # Ask current player for move, and validate its format
            # and its position according to the rules
            new_position = self.view.get_move(self.game.curr_player, self.board) 

            # Add disk            
            self.board.add_disk(self.game.curr_player, new_position)

            # Convert disks           
            self.board.convert_disks_in_all_dirs(new_position)

            # Check if winner

            # Change player
            self.game.change_player()