from model.board import Board
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
        self.dummy_board = Board(brd_size)  # "Local" dummy board object used to simulate moves


    # 1.Look for possible moves, store them in a list of tuples as (position, direction, score)

    def get_possible_moves(self, human_player: Player, board: Board):   
        """Looks for empty cells in the board, and checks each one for convertible disks in 
        its sorroundings by using the function check_and_store_convertible_disks. Possible
        moves are stored in the list of lists self.moves_directions_scores."""
        empty_color_obj = DiskColor(0)
        for row in enumerate(board.mat, 1):  # Traverse the board matrix in search of empty cells.
            for disk in enumerate(row[1], 1):
                if disk[1].color_obj == empty_color_obj:
                    position = (disk[0], row[0])
                    self.check_and_store_convertible_disks(human_player, position, board)                    
   
    def check_and_store_convertible_disks(self, human_player: Player, position, board: Board):  
        """Helper function: Checks if there are sorrounding convertible disks for the given
        empty position; if any are found, saves the empty position (possible move) and its
        corresponding conversion directions in a list."""
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
                        if not (0 <= next_neighbor_position[0] <= board.size - 1 and 0 <= next_neighbor_position[1] <= board.size - 1):  # If next position in direction is out of board dimensions
                            break  
                        elif color_obj_in_next_neighb_pos == self.color_obj:  # If next position in direction has same SimpleAI's color
                            tuple_position = tuple(position)
                            self.moves_directions_scores[tuple_position] = {'trgts_and_dirs': [], 'score': 0}  # In the moves_directions_scores dict, create a new key for the empty position which is a valid move; its value will be a dictionary, as described in the constructor function.
                            self.moves_directions_scores[tuple_position]['trgts_and_dirs'].append([next_neighbor_position, direction])  # Appends the target position and its corresponding direction to the corresponding list value in the empty position sub-dictionary.                            
                            break                                              
                        elif color_obj_in_next_neighb_pos == empty_color_obj:  # If next position in direction is empty                        
                            break
                        elif color_obj_in_next_neighb_pos == human_player.color_obj:  # If next position in direction has opposite player's color
                            continue
            except IndexError:              
                continue



    # 2.Copy the current-state board, "dummy-board" (watch out for aliasing).
    # This function needs to be called from the controller, so as to receive
    # the current board as an argument.
    def clone_current_board(self, board: Board):
        """Helper function: Creates a clone of the current-state board, which will be usued for
        simulating the possible moves found with the method simulate_moves.

        Args:
            board (Board): The board object currently being used in the game.
        """
        self.dummy_board.mat = []  # Reset dummy-board's matrix prior to cloning the current state of the actual game board.
        for row in board.mat:
            self.dummy_board.mat.append(row[:])


    # 3.Convert the disks in the dummy board according to the list created in 1.
    def simulate_moves(self, board: Board):
        """Simulates the resulting boards by playing the moves in the 
        self.moves_directions_scores = [], and appends the score of 
        each resulting simulated board to the corresponding move in
        the mentioned list, for later choosing of the best move available."""
        for move in self.moves_directions_scores:
            self.clone_current_board()
            self.dummy_board.add_disk(self, move)

            # next step: make a function which counts the score of the current board; solve how the returned tuple and it correspondence to the player color will be, 
            # or if it will be a signed integer.

            # 1. need to pass an empty position to the add.disk function of the local dummy board
            # 2. for that, I need a list with these empty positions, which must be valid moves
            # 3. to do this, check what the local list contains and should contain



            pass
            # 1. Update the local dummy current state board (LOCAL BOARD TODAVÍA NO HECHA COMO ATTRIBUTE -> HACERLA)  -DONE
            # 2. Add the disk in question to the local dummy board by using a local copycat board.add_disk function  -SOLVED CREATING A LOCAL BOARD OBJ AS AN ATTRIBUTE
            # 3. Play the move in question in the local dummy board by using a local copycat function of board.convert_disks_in_all_dirs
            # 4. Count the score of the hypothetical board and store it in self.moves_directions_scores
            # 5. Find the move with the maximum score and store it in the self.best_current_move.
        



                    
                 