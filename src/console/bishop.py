from figure import Figure


class Bishop(Figure):
    @property
    def char(self) -> str:
        if self.color.is_white():
            return 'wB'
        return 'bB'
