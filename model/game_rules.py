from model.player import Player


class GameRules:
    ""
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def is_valid_move(player: Player, new_position: tuple, board_size):
        if new_position[0] <= board_size and new_position[1] <= board_size:
            return True
        else: return False
        # Weitere Bewegungsbestägigungen stehen aus
      
    