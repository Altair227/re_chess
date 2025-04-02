from figure import Figure


class Rook(Figure):
    @property
    def char(self) -> str:
        if self.color.is_white():
            return 'wR'
        return 'bR'
