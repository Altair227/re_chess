from figure import Figure


class Queen(Figure):
    @property
    def char(self) -> str:
        if self.color.is_white():
            return 'wQ'
        return 'bQ'
