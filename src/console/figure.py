from src.base import Figure as BaseFigure
from abc import ABC


class Figure(ABC, BaseFigure):
    @property
    def char(self) -> str:
        return '  '
