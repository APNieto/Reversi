from model.disk_color import DiskColor

class Player:
    ""
    def __init__(self, color_obj: DiskColor, score=0) -> None:
        self.color_obj = color_obj
        self.color_name = color_obj.name
        self.color_value = color_obj.value        
        self.score = score      


    def search_valid_moves(self):
        pass