import abc

from tic_tac_toe.logic.models import Mark

# Abstract class that provides the skeleton for concrete subclasses
class Player(metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark) -> None:
        self.mark = mark
