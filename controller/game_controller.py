from model.game import ReversiGame
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
            
            self.board.mat = self.game.convert_disks((1,1), (7,1), (1,0), self.board.mat)  # TEST CODE FOR CONVERTION FUNCTION IN gmae.py
            

            #TEST Print the color attributes of the board matrix (disk objects)
            self.board.display()            

            # Show score
            self.game.calculate_scores()
            self.view.display_score(self.game.players_list)

            # Ask current player for move, and validate its format
            # and its position according to the rules
            new_position = self.view.get_move(self.game.curr_player, self.board)

            # Add disk            
            self.board.add_disk(self.game.curr_player, new_position)

            # Check if winner

            # Change player
            self.game.change_player()