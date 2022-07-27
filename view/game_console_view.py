from view.game_view import GameView
from model.player import Player


class GameConsoleView(GameView):
    ""
    def __init__(self, board_size=8) -> None:
        super().__init__(board_size)

    def display_welcome_meessage(self):
        print("\nWelcome to Reversi!")
        print("====================")

    def display_score(self, player_1: Player, player_2: Player):
        ""
        score_player_1 = player_1.calculate_score()
        score_player_2 = player_2.calculate_score()
        print(f'\nScore Player 1: {score_player_1}'
        f'\nScore Player 2: {score_player_2}')

    def get_move(self, player: Player):
        ""
        self.users_move_raw = input(f'Player {(player.color).title()}, '
        'please enter the "x,y" coordinates of your new disk ("" symbols not necessary): ')
        is_input_correct = False
        while not is_input_correct:
            if len(self.users_move_raw) == 3 and self.users_move_raw[1] == ',':
                try:
                    self.users_move = tuple(int(self.users_move_raw[0]), int(self.users_move_raw[2]))
                    is_input_correct = True
                except ValueError:
                    self.users_move_raw = input('The pair of coordinates '
                    'must be in the format "x,y" ("" not needed): ')
        return self.users_move  

    def display_winner(self, player_winner: Player, player_loser: Player):
        print(f'\nWinner is {player_winner} with a score of {player_winner.score}.'
        f'\nLoser is {player_loser} with a score of {player_loser.score}.')

        