from bishop import Bishop
from pawn import Pawn
from rook import Rook
from colors import BlackColor, WhiteColor
from king import King
from queen import Queen
from knight import Knight
from figure import Figure

COLS = 8
ROWS = 8


class Board:
    __PAWN = Pawn
    __BISHOP = Bishop
    __ROOK = Rook
    __KING = King
    __QUEEN = Queen
    __KNIGHT = Knight

    def __init__(self):
        self.__board = []
        self.__color = WhiteColor()
        for _ in range(COLS):
            self.__board.append([None] * COLS)
        for col in range(COLS):
            self.set_item(1, col, self.__PAWN(WhiteColor()))
            self.set_item(ROWS - 2, col, self.__PAWN(BlackColor()))
        for col in [0, COLS - 1]:
            self.set_item(0, col, self.__ROOK(WhiteColor()))
            self.set_item(ROWS - 1, col, self.__ROOK(BlackColor()))
        for col in [2, COLS - 3]:
            self.set_item(0, col, self.__BISHOP(WhiteColor()))
            self.set_item(ROWS - 1, col, self.__BISHOP(BlackColor()))
        for col in [1, COLS - 2]:
            self.set_item(0, col, self.__KNIGHT(WhiteColor()))
            self.set_item(ROWS - 1, col, self.__KNIGHT(BlackColor()))
        self.set_item(0, COLS - 4, self.__KING(WhiteColor()))
        self.set_item(ROWS - 1, COLS - 4, self.__KING(BlackColor()))
        self.set_item(0, COLS - 5, self.__QUEEN(WhiteColor()))
        self.set_item(ROWS - 1, COLS - 5, self.__QUEEN(WhiteColor()))


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

    def set_item(self, row: int, col: int, figure: Figure | None):
        if not self.validate(row, col):
            return None
        self.__board[row][col] = figure

    def move(self, row_start: int, col_start: int, row_end: int, col_end: int):
        self.set_item(row_end, col_end, self.get_item(row_start, col_start))
        self.set_item(row_start, col_start, None)
        self.__color = self.__color.get_opponent()
