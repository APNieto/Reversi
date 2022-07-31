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
            
            #TEST Print the color attributes of the board matrix (disk objects)
            self.board.display()            

            # Show score
            self.game.calculate_scores()
            self.view.display_score(self.game.players_list)

            # Ask current player for move
            new_position = self.view.get_move(self.game.curr_player)

            # TEST Dummy check and add disk
            if self.game.is_valid_move(self.game.curr_player, new_position):            
                self.board.add_disk(self.game.curr_player, new_position)

            # Check if winner

            # Change player
            self.game.change_player()