from .figure import Figure


class Knight(Figure):
    @property
    def char(self) -> str:
        if self.color.is_white():
            return 'wN'
        return 'bN'

    def can_move(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:

        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        return row_diff == 2 and col_diff == 1 or row_diff == 1 and col_diff == 2
