from model.disk_color import DiskColor

class Disk:
    def __init__(self, color_obj: DiskColor):
        self.color_obj = color_obj        
    
    def change_color(self):
        self.color_obj = DiskColor(3 - self.color_obj.value)