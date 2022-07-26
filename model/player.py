from model.disk_color import DiskColor

class Player:
    ""

    def __init__(self, color: DiskColor, score=0) -> None:
        self.color = color.name
        self.color_value = color.value
        self.score = score
        self.available_moves = []

    