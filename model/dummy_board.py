from model.board import Board

class DummyBoard(Board):

    def __init__(self, size: int = 8) -> None:
        super().__init__(size)


    def convert_disks_in_all_dirs(self, start_pos, targets_and_directions):
        """Disk conversion function used for the simulatoin of possible boards
        by the SimpleAI player. Overrides the board's original function, with a
        general targets_and_directions argument, not dependant on the GameRules class.

        Args:
            start_pos (tuple): empty position in board where the SimpleAI plays its simulated move.
            targets_and_directions (list): list of 2-value tuples, first is target direction and the second is the conversion direction
        """
        for tuple in targets_and_directions:
            self.convert_disks_in_one_dir(start_pos, tuple[0], tuple[1])