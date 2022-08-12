from model.disk_color import DiskColor

class Player:
    ""
    def __init__(self, color_obj: DiskColor, score=0) -> None:
        self.color_obj = color_obj
        self.color_name = color_obj.name    # Acceptable only because these values will not change
        self.color_value = color_obj.value  # unlike the Disk object case, where the "sub-object"
        self.score = score                  # attribute did change but this was not reflected in the original object