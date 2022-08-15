from model.dummy_board import DummyBoard
from model.disk_color import DiskColor
from model.player import Player
from model.game_rules import GameRules


class SimpleAI(Player):
    ""
    def __init__(self, color_obj: DiskColor, score=0, brd_size=None) -> None:
        super().__init__(color_obj, score)

        # First attribute is a dictionary containing each empty position which is a valid move
        # as a key; each one of these keys has a sub-dictionary with 2 keys: one is a list 
        # containing the target positions and their corresponding directions as a list of lists,
        # and the other is the corresponding score of the move in said empty position.
        # Format would be as follows:
        # self.moves_directions_scores = {empty_position: {target position and directions: list of lists, score: integer}} 
        self.moves_directions_scores = {}  
        self.best_current_move = ()
        self.dummy_board = DummyBoard(brd_size)  # "Local" dummy board object used to simulate moves


    # 1.Look for possible moves, store them in the local dictionary attribute moves_directions_scores.
    def get_possible_moves(self, human_player: Player, board):   
        """Looks for empty cells in the actual in-use board, and checks each one for convertible disks in 
        its sorroundings by using the function check_and_store_convertible_disks. Possible
        moves are stored in the list of lists self.moves_directions_scores."""
        empty_color_obj = DiskColor(0)
        for row in enumerate(board.mat, 1):  # Traverse the board matrix in search of empty cells.
            for disk in enumerate(row[1], 1):
                if disk[1].color_obj == empty_color_obj:
                    position = (disk[0], row[0])
                    self.check_and_store_convertible_disks(human_player, position, board)                    
   

    def check_and_store_convertible_disks(self, human_player: Player, position, board):  
        """Helper function: Checks if there are sorrounding convertible disks for the given
        empty position; if any are found, saves the empty position (possible move) and its
        corresponding conversion directions in the moves_directions_scores dictionary."""
        empty_color_obj = DiskColor(0)
        self.moves_directions_scores = []  # Resets the list of possible moves for each new call/turn.
        position = (position[0] - 1, position[1] - 1)  # Adjust coordinates for access in actual matrix, with indices which start at 0
        for direction in GameRules.directions:            
            neighbor_position = (position[0] + direction[0], position[1] + direction[1])
            next_neighbor_position = neighbor_position  # For debugging purposes: keep a fixed variable (neighbor) with the first opposite disk, and a second one (next_neighbor) for further searching.
            try:
                if board.mat[neighbor_position[1]][neighbor_position[0]].color_obj == human_player.color_obj:  # Direction is valid if new_position has a neighbor with a disk of opposite color
                    while True:
                        next_neighbor_position = (next_neighbor_position[0] + direction[0], next_neighbor_position[1] + direction[1])  # Advance one further cell in the current tested direction
                        color_obj_in_next_neighb_pos = board.mat[next_neighbor_position[1]][next_neighbor_position[0]].color_obj
                        # If next position in direction is out of board dimensions
                        if not (0 <= next_neighbor_position[0] <= board.size - 1 and 0 <= next_neighbor_position[1] <= board.size - 1):
                            break  
                        elif color_obj_in_next_neighb_pos == self.color_obj:  # If next position in direction has same SimpleAI's color
                            tuple_position = tuple(position)
                            # In the moves_directions_scores dict, create a new key for the empty position which is a valid move; its value will be a dictionary, as described in the constructor function.
                            self.moves_directions_scores[tuple_position] = {'trgts_and_dirs': [], 'score': 0}  
                            # Appends the target position and its corresponding direction to the corresponding list value in the empty position sub-dictionary.                            
                            self.moves_directions_scores[tuple_position]['trgts_and_dirs'].append([next_neighbor_position, direction])
                            break                                              
                        elif color_obj_in_next_neighb_pos == empty_color_obj:  # If next position in direction is empty                        
                            break
                        elif color_obj_in_next_neighb_pos == human_player.color_obj:  # If next position in direction has opposite player's color
                            continue
            except IndexError:              
                continue


    # 2.Convert the disks in the dummy board according to the list created in 1.
    def simulate_moves(self, players_list, curr_board):
        """Simulates the resulting boards by playing the moves in the 
        self.moves_directions_scores = [], and appends the score of 
        each resulting simulated board to the corresponding move in
        the mentioned list, for later choosing of the best move available."""
        for move in self.moves_directions_scores:
            self.clone_current_board(curr_board)
            self.dummy_board.add_disk(self, move)
            self.dummy_board.convert_disks_in_all_dirs(move, self.moves_directions_scores[move]['trgts_and_dirs'])
            score_of_move = self.calc_score_in_dummy_board(players_list)
            self.moves_directions_scores[move]['score'] = score_of_move

            # Steps carried out:
            # 1. Update the local dummy current state board (LOCAL BOARD TODAVÍA NO HECHA COMO ATTRIBUTE -> HACERLA)  -DONE
            # 2. Add the disk in question to the local dummy board by using a local copycat board.add_disk function  -SOLVED CREATING A LOCAL BOARD OBJ AS AN ATTRIBUTE
            # 3. Play the move in question in the local dummy board by using a local copycat function of board.convert_disks_in_all_dirs
            # 4. Count the score of the hypothetical board and store it in self.moves_directions_scores


    def clone_current_board(self, curr_board):
        """Helper function: Creates a clone of the current-state board, which will be usued for
        simulating the possible moves found with the method simulate_moves.

        Args:
            board (Board): The board object currently being used in the game.
        """
        self.dummy_board.mat = []  # Reset dummy-board's matrix prior to cloning the current state of the actual game board.
        for row in curr_board.mat:
            self.dummy_board.mat.append(row[:])


    def calc_score_in_dummy_board(self, players_list):
        """Helper function: calculates the score of the AI player based on the current dummy board.
        Result is given as a single signed integer, being a result of (AI score - human player score)."""
        for player in players_list:
            player.calculate_score(self.dummy_board)
            if isinstance(player, SimpleAI):
                AI_score = player.score
            else:
                human_score = player.score
        AI_overall_score = AI_score - human_score
        return AI_overall_score


    # 3. Finds the move/position in the current board which produces the highest score.
    def find_best_move(self):
        """Finds the move with the maximum score from the moves_directions_scores
        dictionary attribute and store it in the self.best_current_move attribute.
        Returns:
            tuple: x,y coordinate which produces the highest score.
        """
        max_score = 0
        for move in self.moves_directions_scores:
            if self.moves_directions_scores[move]['score'] > max_score:
                max_score = self.moves_directions_scores[move]['score']
                best_move = move
        return best_move


# 1. Put it in words
# 2. Put it in code