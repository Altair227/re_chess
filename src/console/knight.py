from figure import Figure


class Knight(Figure):
    @property
    def char(self) -> str:
        if self.color.is_white():
            return 'wN'
        return 'bN'
