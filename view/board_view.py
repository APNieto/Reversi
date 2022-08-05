from abc import ABC, abstractmethod
from model.board import Board

class BoardView:

    def __init__(self, board: Board):
        self.board = board
    
    def display_board(self):
        pass

    def conchatuma(self):
        pass