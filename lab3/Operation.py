from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def get_sign(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def estimate(self, a, b):
        pass