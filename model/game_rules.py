from model.disk_color import DiskColor
from model.player import Player

class GameRules:
    ""

    end_points_and_directions = []  # Collects the end points and its corresponding direction as tuples, for accurate
                                    # conversion of disks between these end points and the given user's initial point    
    error_codes = {0: 'The given position if out of the board\'s dimensions.', 
                   1: 'The given position is already occupied by another disk.', 
                   2: 'There are no sorrounding opponent\'s disks to be converted in the given position.'}
    last_error_code = 0
    

    def __init__(self) -> None:
        pass


    @staticmethod
    def is_valid_move(player: Player, new_position: tuple, board, game_mode: int):        
        if not GameRules.is_new_pos_within_board(new_position, board.size):
            GameRules.last_error_code = 0
            return False        
        if not GameRules.is_new_pos_available(new_position, board):
            GameRules.last_error_code = 1
            return False
        if game_mode == 1:
            if not GameRules.exist_and_store_convertible_disks(player, new_position, board):
                GameRules.last_error_code = 2
                return False
        elif game_mode == 2:
            GameRules.exist_and_store_convertible_disks(player, new_position, board)
        return True


    @staticmethod
    def is_new_pos_within_board(new_position: tuple, board_size):        
        if new_position[0] <= board_size and new_position[1] <= board_size:
            return True
        else: return False        

        
    @staticmethod
    def is_new_pos_available(new_position: tuple, board):
        new_position = (new_position[0] - 1, new_position[1] - 1)  # Adjust for access in actual matrix indexes which start at 0       
        board_cell = board.mat[new_position[1]][new_position[0]]        
        if board_cell.color_obj.value == 0:
            return True
        else: return False
   

    @staticmethod
    def exist_and_store_convertible_disks(player: Player, new_position, board):  
        """Checks if there are sorrounding convertible disks for the given position, 
        and saves these found convertible disks and the corresponding direction in a
        static list."""
        opposite_player_color_obj = DiskColor(3 - player.color_value)   
        empty_color_obj = DiskColor(0)
        GameRules.end_points_and_directions = []  # List of tuples containing the end point and direction where disk conversions can be made relative to the new position given by the player (reset for each new turn)
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        new_position = (new_position[0] - 1, new_position[1] - 1)  # Adjust for access in actual matrix indexes which start at 0
        exist_convertbl_disks = False
        for direction in directions:            
            neighbor_position = (new_position[0] + direction[0], new_position[1] + direction[1])
            next_neighbor_position = neighbor_position  # Purpose is to keep a variable containing the first opposite disk, and a second one for further searching, 
                                                        # for debugging purposes.

            # ////DEBUG PRINT////
            print(f'\n////DEBUG PRINT////\ngame_rules.py - neighbor_position: before checking if it is an opposite color neighbor'
            f'\n{(neighbor_position[0], neighbor_position[1])}, in direction: {direction}')

            try:
                if board.mat[neighbor_position[1]][neighbor_position[0]].color_obj == opposite_player_color_obj:  # Direction is valid if new_position has a neighbor with a disk of opposite color
                    while True:

                        # ////DEBUG PRINT////
                        print(f'\n////DEBUG PRINT////\nGameRules.end_points_and_directions: {GameRules.end_points_and_directions}')

                        # ////DEBUG PRINT////
                        print(f'\n////DEBUG PRINT////\ngame_rules.py - neighbor_position: ***AFTER*** confirming this is an opposite color neighbor'
                        f'\nneighbor_position: {neighbor_position}, in direction: {direction}')

                        next_neighbor_position = (next_neighbor_position[0] + direction[0], next_neighbor_position[1] + direction[1])  # Advance one further cell in the current tested direction

                        print(f'\n////DEBUG PRINT////\nnext_neighbor_position: {next_neighbor_position}')
                        print(f'\n////DEBUG PRINT////\ndirection: {direction}')


                        color_obj_in_next_neighb_pos = board.mat[next_neighbor_position[1]][next_neighbor_position[0]].color_obj
                        if not (0 <= next_neighbor_position[0] <= board.size - 1 and 0 <= next_neighbor_position[1] <= board.size - 1):  # If +1 in same direction is out of board
                            print(f'\n////DEBUG PRINT////\nnext_neighbor_position did not pass the 0 <= n <= size boundaries test.')
                            break  # Cannot insert a disk here because it is out of board dimensions
                        elif color_obj_in_next_neighb_pos == player.color_obj:  # If +1 in same direction has same player's color
                            GameRules.end_points_and_directions.append((next_neighbor_position, direction))
                            exist_convertbl_disks = True
                            break                                              
                        elif color_obj_in_next_neighb_pos == empty_color_obj:  # If +1 in same direction is empty                        
                            break
                        elif color_obj_in_next_neighb_pos == opposite_player_color_obj:  # If +1 in same direction has opposite player's color
                            continue
            except IndexError:
                
                #  DEBUG PRINT
                print('\n////DEBUG PRINT////\ngame_rules.py: IndexError when accessing board.mat. Expected behavior\n')
                
                continue
        return exist_convertbl_disks


    @staticmethod
    def exist_convertible_disks_overall(player: Player, board):        
        are_convertible_disks_overall = False
        empty_color_obj = DiskColor(0)
        for row in enumerate(board.mat, 1):
            for disk in enumerate(row[1], 1):
                if disk[1].color_obj == empty_color_obj:
                    position = (disk[0], row[0])
                    if GameRules.exist_convertible_disks_helper(player, position, board):
                        are_convertible_disks_overall = True
                        return are_convertible_disks_overall
        return are_convertible_disks_overall
                    

    @staticmethod
    def exist_convertible_disks_helper(player: Player, position, board):
        """Helper Function"""
        opposite_player_color_obj = DiskColor(3 - player.color_value)
        empty_color_obj = DiskColor(0)
        valid_directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        position = (position[0] - 1, position[1] - 1)  # Adjust for access in actual matrix indexes which start at 0
        exist_convertbl_disks = False
        for direction in valid_directions:            
            neighbor_position = (position[0] + direction[0], position[1] + direction[1])
            try:
                if board.mat[neighbor_position[1]][neighbor_position[0]].color_obj == opposite_player_color_obj:  # Direction is valid if new_position has a neighbor with a disk of opposite color
                    while True:
                        neighbor_position = (neighbor_position[0] + direction[0], neighbor_position[1] + direction[1])  # Advance one further cell in the current tested direction
                        color_obj_in_neighb_pos = board.mat[neighbor_position[1]][neighbor_position[0]].color_obj
                        if neighbor_position[0] > board.size - 1 or neighbor_position[1] > board.size - 1:  # If +1 in same direction is out of board
                            break  # Cannot play here because next available spot is out of the board dimensions
                        elif color_obj_in_neighb_pos == player.color_obj:  # If +1 in same direction has same player's color
                            exist_convertbl_disks = True
                            return exist_convertbl_disks                                                   
                        elif color_obj_in_neighb_pos == empty_color_obj:  # If +1 in same direction is empty                        
                            break
                        elif color_obj_in_neighb_pos == opposite_player_color_obj:  # If +1 in same direction has opposite player's color
                            continue
            except IndexError:
                continue
        return exist_convertbl_disks