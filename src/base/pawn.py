from figure import Figure


class Pawn(Figure):
    def can_move(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:
        if from_col != to_col:
            return False
        if self.color.is_white():
            direction = 1
        else:
            direction = -1
        accepted_rows = [from_row + direction]
        if self.color.is_white() and from_row == 1 or self.color.is_black() and from_row == 6:
            accepted_rows.append(from_row + direction * 2)
        if to_row not in accepted_rows:
            return False
        for row in range(from_row + direction, to_row, direction):
            if board.get_item(row, from_col) is not None:
                return False
        return True

    def can_attack(self,
                   board,
                   from_row: int,
                   from_col: int,
                   to_row: int,
                   to_col: int
                   ) -> bool:
        if abs(from_col - to_col) != 1:
            return False
        if self.color.is_white():
            direction = 1
        else:
            direction = -1
        return to_row - from_row == direction
