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
            
            #Print TEST dummy board
            self.board.display()            

            # Show score
            for player in self.game.players_list:
                self.game.calculate_score(player)            
                self.view.display_score(player.score)

            # Ask current player for move
            move = self.view.get_move(self.game.curr_player)

            # TEST Dummy check and add disk
            if self.game.is_valid_move(self.game.curr_player, move):            
                self.board.add_disk()

            # Check if winner

            # Change player