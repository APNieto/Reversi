from model.disk_color import DiskColor
from model.player import Player
from model.board import Board

class GameRules:
    ""
    def __init__(self) -> None:
        pass


    @staticmethod
    def is_valid_move(player: Player, new_position: tuple, board: Board):
        boundary_for_conversion = GameRules.are_possible_conversions(player, new_position, board)
        if GameRules.is_within_board(new_position, board.size) and boundary_for_conversion:
            return boundary_for_conversion
        else: return False


    @staticmethod
    def is_within_board(new_position: tuple, board_size):
        if new_position[0] <= board_size and new_position[1] <= board_size:
            return True
        else: return False
   

    @staticmethod
    def are_possible_conversions(player: Player, new_position, board: Board):  
        opposite_player_color_obj = DiskColor(3 - player.color_value)
        print(f'Opposite color: {opposite_player_color_obj.name}.')  # TEST print opposite color in game_rules.py
        empty_color_obj = DiskColor(0)
        valid_directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        new_position = (new_position[0] - 1, new_position[1] - 1)  # Adjust for access in actual matrix indexes which start at 0
        for direction in valid_directions:            
            neighbor_position = (new_position[0] + direction[0], new_position[1] + direction[1])
            if board.mat[neighbor_position[1]][neighbor_position[0]].color_obj == opposite_player_color_obj:  # Direction is valid if new_position has a neighbor with a disk of opposite color
                print(f'The new position IS next to a disk of opposite color in direction {direction}.') # TEST PRINT
                while True:
                    neighbor_position = (neighbor_position[0] + direction[0], neighbor_position[1] + direction[1])  # Advance one further cell in the current tested direction
                    color_obj_in_neighb_pos = board.mat[neighbor_position[1]][neighbor_position[0]].color_obj
                    if neighbor_position[0] > board.size - 1 or neighbor_position[1] > board.size - 1:  # If +1 in same direction is out of board
                        print('Probing out of board.')  # TEST PRINT
                        return False  # Cannot play here because next avilable 
                    elif color_obj_in_neighb_pos == player.color_obj:  # If +1 in same direction has same player's color
                        print('Probing found same color > VALID SPOT > saves this destination spot, origin spot and direction.')  # TEST PRINT
                        boundary_for_conversion = neighbor_position
                        return boundary_for_conversion  # This position needs to be saved so to know the boundaries of the disk conversion which need to take place
                    elif color_obj_in_neighb_pos == empty_color_obj:  # If +1 in same direction is empty                        
                        print('Probing found empty spot > breaks loop.')  # TEST PRINT                                                
                        return False
                    elif color_obj_in_neighb_pos == opposite_player_color_obj:  # If +1 in same direction has opposite player's color
                        print('Probing opposite color > continue probing.')  # TEST PRINT
                        continue
            else:
                print(f'The new position is NOT next to a disk of opposite color in direction {direction}.')  # TEST PRINT

                        # TODO: .test last code
                        #       .save valid directions in static dict in player with key: direction, value: list of 2 tuples with start and end positions,
                        #       for later easier disk convertion
                
        # Check if next slot is: 1. empty: return True 2. has opposite: keep looping  3. has same color: return False  4. out of board: return False

    @staticmethod
    def is_within_available_moves(new_position: tuple):
        return True