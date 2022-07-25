from model.disk_color import DiskColor

class Disk:
    def __call__(self, color: DiskColor, position: tuple) -> Any:
        self.color = color
        self.position = position
    
    def change_color():
        self.color = 3 - self.color
