from .colors import Color


class Figure:
    def __init__(self, color: Color):
        self.__color = color

    @property
    def char(self) -> str:
        return '  '

    @property
    def color(self) -> Color:
        return self.__color

    def can_move(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:
        return False

    def can_attack(self,
                   board,
                   from_row: int,
                   from_col: int,
                   to_row: int,
                   to_col: int
                   ) -> bool:
        return self.can_move(board, from_row, from_col, to_row, to_col)
