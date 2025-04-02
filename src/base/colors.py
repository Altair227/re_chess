class Color:
    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__

    @staticmethod
    def is_white() -> bool:
        return False

    @staticmethod
    def is_black() -> bool:
        return False

    @staticmethod
    def get_opponent():
        return Color()


class BlackColor(Color):
    @staticmethod
    def is_white() -> bool:
        return False

    @staticmethod
    def is_black() -> bool:
        return True

    @staticmethod
    def get_opponent():
        return WhiteColor()


class WhiteColor(Color):
    @staticmethod
    def is_white() -> bool:
        return True

    @staticmethod
    def is_black() -> bool:
        return False

    @staticmethod
    def get_opponent():
        return BlackColor()
