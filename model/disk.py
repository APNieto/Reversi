from model.disk_color import DiskColor

class Disk:
    def __init__(self, color_obj: DiskColor):
        self.color_obj = color_obj
        self.color_name = color_obj.name
    
    def change_color(self):
        self.color_obj = DiskColor(3 - self.color.value)


