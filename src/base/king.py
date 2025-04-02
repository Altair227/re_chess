from figure import Figure


class King(Figure):
    def can_move(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if row_diff <= 1 and col_diff <= 1:
            return True
        return False
