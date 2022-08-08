from model.game import ReversiGame
from model.game_rules import GameRules
from view.game_view import GameView

class GameController:

    def __init__(self, game: ReversiGame, view: GameView) -> None:
        self.game = game
        self.view = view


    def run_game(self):

        self.play_again = True

        while self.play_again:

            self.view.display_welcome_meessage()
            board_size = self.view.get_board_size()        
            self.game.create_board(board_size)
            self.board = self.game.board
            self.view.pass_board_to_board_cons_view()
            game_mode = self.view.get_game_mode()
            self.game.game_mode = game_mode
            self.no_available_moves_counter = 0  # If this counter reaches 2, it means there were no available movements
                                            # for 2 consecutive rounds, so game is over and a winner must be determined.
            has_winner = False

            while not has_winner:            
                
                # DEBUG PRINT: Print the board matrix
                # print('\n//DEBUG PRINT//\n\ngame_controller.py - self.board.mat')  
                # for row in self.board.mat:
                #     for disk in row:
                #         print(disk.color_obj.name, end='')
                #     print('')
                
                # Display the board
                self.view.display_board()

                # Show score
                self.game.calculate_scores()
                self.view.display_score(self.game.players_list)

                
                # Check if winner in case:
                # 1. Board is full
                is_brd_full = self.board.is_board_full()
                if is_brd_full:
                    self.view.display_winner(self.game.players_list)
                    has_winner = True
                    self.play_again = self.view.ask_for_replay()
                    continue   

                # DEBUG PRINT
                # print(f'\n//DEBUG PRINT//\ngame_controller - self.no_available_moves_counter: {self.no_available_moves_counter}\n')
                
                # 2. There are no available moves for 2 rounds in a row
                if self.no_available_moves_counter == 2:
                    self.view.display_winner(self.game.players_list)
                    has_winner = True
                    self.play_again = self.view.ask_for_replay()
                    continue                


                # Check for available moves; in case none, change players
                if not GameRules.exist_convertible_disks_overall(self.game.curr_player, self.board):
                    self.game.change_player()
                    self.no_available_moves_counter += 1
                    self.view.print_skip_turn(self.game.curr_player)
                    continue
                else:
                    self.no_available_moves_counter = 0


                # Ask current player for move and validate its format
                # If it is a valid move, then add the disk to the bord
                while True:  # TODO Generate different appropriate error messages for each type of invalid input, as with a dictionary, for example                
                    new_position = self.view.get_move(self.game.curr_player, self.board) 
                    if GameRules.is_valid_move(self.game.curr_player, new_position, self.board, self.game.game_mode):
                        self.board.add_disk(self.game.curr_player, new_position)
                        break
                    else:
                        print(GameRules.error_codes[GameRules.last_error_code])

                # DEBUG PRINT
                print(f'\n//DEBUG PRINT//\ngame_controller.py - GameRules.end_points_and_directions'
                f'\n{GameRules.end_points_and_directions}')  
                                        
                # Convert disks           
                self.board.convert_disks_in_all_dirs(new_position)

                # Change player
                self.game.change_player()