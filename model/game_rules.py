from model.player import Player


class GameRules:
    ""
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def is_valid_move(player: Player, position: tuple, board_size):
        if position[0] <= board_size and position[1] <= board_size:
            return position in GameRules.list_available_moves(player)
        else: return False
      
       
    @staticmethod
    def list_available_moves(player: Player):
        """Returns list with available positions for the given player's next move"""
        pass