from model.disk_color import DiskColor

class Disk:
    def __init__(self, color: DiskColor):
        self.color = color                
        self.color_name = color.name
    
    def change_color(self):
        self.color = DiskColor(3 - self.color.value)


