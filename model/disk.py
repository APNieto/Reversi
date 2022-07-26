from model.disk_color import DiskColor

class Disk:
    def __init__(self, color: DiskColor, position: tuple):
        self.color = color
        self.position = position
    
    def change_color(self):
        self.color = DiskColor(3 - self.color.value)


