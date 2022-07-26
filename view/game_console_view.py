from model.board import Board
from model.game import ReversiGame
from model.player import Player
from view.game_view import GameView
from view.board_console_view import BoardConsoleView


class GameConsoleView(GameView):
    ""
    def __init__(self, game: ReversiGame, board_size=8) -> None:
        super().__init__(game, board_size)         


    def display_welcome_meessage(self):
        print("\n\nWelcome to Reversi!")
        print("===================")


    def get_player_mode(self):
        """Lets the user decide whether he/she wants to play against another
        real player (2-player game) or against the computer. Asks for 
        an integer input corresponding to each one of these "player modes".

        Returns:
            tuple: a two-value tuple, whose first value represents the player mode and
            the second one the color of the human player in case vs-computer player mode is chosen.
        """
        while True:
            player_mode = input('\nPlease choose the player mode: \n'
            '1. Play against the computer\n'
            '2. 2-player mode\n'
            'Please enter your choice: ')
            if player_mode == '2':
                return int(player_mode), 0
            elif player_mode == '1':
                break
            else:
                print('\n* Invalid input. Please enter "1" or "2". *')
        
        while True:
            color_choice = input('\nPlease choose with which color you want to play: b (for black) or w (for white): \n'
                'Please enter your choice: ')
            if color_choice == 'b' or color_choice == 'w':
                return int(player_mode), color_choice
            else:
                print('\n* Invalid input. Please enter "b" or "w". *')


    def get_game_mode(self):
        while True:
            game_mode = input('\nPlease choose the game mode, there are 2 available: \n'
            '1. New disks must produce new flips\n'
            '2. New disks don\'t necessarily have to produce new flips\n'
            'Please enter your choice: ')            
            if game_mode == '1' or game_mode == '2':                        
                return int(game_mode)
            else:
                print('\n* Invalid input. Please enter "1" or "2". *')


    def pass_board_to_board_cons_view(self):
        self.board_view = BoardConsoleView(self.game.board)
   

    def get_board_size(self):
        ""
        while True:
            board_size = input('\nPlease enter the desired board size (even integer): ')
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


    def get_move(self, player: Player, board):
        """ Gets move from the user. Only task done here is user input 
        and formatting into a tuple of the kind (int, int), regardless
        of the nr of digits each int has.
        """
        while True:
            users_move_raw = input(f'\nPlayer {(player.color_name).title()}, '
            'please enter the "x,y" coordinates of your new disk: ')
            comma_index = users_move_raw.find(',')
            if comma_index != -1:
                dig1 = users_move_raw[:comma_index]
                dig2 = users_move_raw[comma_index + 1:]            
            else:
                print('Invalid input.')
                continue

            try:
                if int(dig1) and int(dig2):
                    users_move = (int(dig1), int(dig2))
                    return users_move
            except ValueError:
                print('Invalid input.')
                continue


    def display_board(self):
        self.board_view.display_board()


    def print_skip_turn(self, player):
        print(f'\nThere are no moves available for the current player {(player.color_name).title()}.'
        ' Skip turn!')
        input('Press Enter to continue...')


    def display_winner(self, players_list):
        scores = [players_list[0].score, players_list[1].score]
        idx_max_score = scores.index(max(scores))        
        idx_min_score = scores.index(min(scores))
       
        if idx_max_score != idx_min_score:
            result_text = (f'**Winner** is player {players_list[idx_max_score].color_name.title()} with a score of {players_list[idx_max_score].score}.'
            f'\nLoser is player {players_list[idx_min_score].color_name.title()} with a score of {players_list[idx_min_score].score}.\n') 
            print('\n\n**************** Game ended! ****************')
            print(result_text)
            return result_text                
        else:
            result_text = f'It\'s a tie with score {players_list[idx_max_score].score} for both players.\n'
            print('\n\n**************** Game ended! ****************\n')            
            print(result_text)
            return result_text   

    
    def ask_for_replay(self):
        replay = input('\nWould you like to play again? y/n: ')
        if replay.lower() == 'y':
            return True
        else: 
            print('\nMumbye!')
            return False