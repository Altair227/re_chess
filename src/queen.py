from .figure import Figure


class Queen(Figure):
    @property
    def char(self) -> str:
        if self.color.is_white():
            return 'wQ'
        return 'bQ'

    def can_move(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if from_row != to_row and from_col != to_col and row_diff != col_diff:
            return False
        row_step = 0
        col_step = 0
        if from_row == to_row:
            col_step = 1 if to_col > from_col else -1
        elif from_col == to_col:
            row_step = 1 if to_row > from_row else -1
        else:
            row_step = 1 if from_row < to_row else -1
            col_step = 1 if from_col < to_col else -1
        row = from_row + row_step
        col = from_col + col_step
        while row != to_row and col != to_col:
            if board.get_item(row, col) is not None:
                return False
            row += row_step
            col += col_step
        return True

