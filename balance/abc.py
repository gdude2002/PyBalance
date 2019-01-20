from abc import ABC, abstractmethod


class Window(ABC):
    @abstractmethod
    def setup(self):
        return NotImplemented

    @abstractmethod
    def show(self):
        return NotImplemented
