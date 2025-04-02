from figure import Figure


class Pawn(Figure):
    @property
    def char(self) -> str:
        if self.color.is_white():
            return 'wP'
        return 'bP'