from figure import Figure


class King(Figure):
    @property
    def char(self) -> str:
        if self.color.is_white():
            return 'wK'
        return 'bK'
