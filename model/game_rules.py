from model.player import Player


class GameRules:
    ""
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def is_valid_move(player: Player, position: tuple, board_size):
        if position[0] <= board_size and position[1] <= board_size:
            return GameRules.check_available_moves(player, position)                
        else: return False
      
       
    @staticmethod
    def check_available_moves(player: Player, position: tuple):
        return True