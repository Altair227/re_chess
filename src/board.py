from .pawn import Pawn
from .colors import BlackColor, WhiteColor

class Board:
    def __init__(self):
        self.__board = []
        self.__color = WhiteColor()
        for _ in range(8):
            self.__board.append([None] * 8)
        for col in range(8):
            self.__board[1][col] = Pawn(WhiteColor())
            self.__board[6][col] = Pawn(BlackColor())

    @property
    def color(self) -> BlackColor | WhiteColor:
        return self.__color

    @staticmethod
    def validate(row: int, col: int) -> bool:
        return 0 <= row < 8 and 0 <= col < 8

    @staticmethod
    def convert(point: str) -> tuple[int, int] | None:
        if len(point) < 2:
            return
        col = ord(point[0]) - ord('A')
        row = int(point[1]) - 1
        return row, col

    def get_item(self, row: int, col: int):
        if not self.validate(row, col):
            return None
        return self.__board[row][col]
