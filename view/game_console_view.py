from model.game import ReversiGame
from model.player import Player
from view.game_view import GameView



class GameConsoleView(GameView):
    ""
    def __init__(self, game: ReversiGame, board_size=8) -> None:
        super().__init__(game, board_size)      


    def display_welcome_meessage(self):
        print("\nWelcome to Reversi!")
        print("===================\n")


    def display_score(self, players_list: list):
        ""
        print('\n***Scores***')
        for player in players_list:
            print(f'Player {(player.color_name).title()}: {player.score}')


    def get_move(self, player: Player):
        ""
        self.users_move_raw = input(f'\nPlayer {(player.color_name).title()}, '
        'please enter the "x,y" coordinates of your new disk: ')
        is_input_correct = False
        while not is_input_correct:
            if len(self.users_move_raw) == 3 and self.users_move_raw[1] == ',':
                try:
                    self.users_move = tuple((int(self.users_move_raw[0]), int(self.users_move_raw[2])))
                    is_input_correct = True
                except ValueError:
                    self.users_move_raw = input('The pair of coordinates '
                    'must be in the format "x,y" ("" not needed): ')
        return self.users_move  


    def display_winner(self, player_winner: Player, player_loser: Player):
        print(f'\nWinner is {player_winner} with a score of {player_winner.score}.'
        f'\nLoser is {player_loser} with a score of {player_loser.score}.')

        