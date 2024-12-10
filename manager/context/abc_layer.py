from abc import ABC, abstractmethod


error = Exception("This class is abstract and cannot be instantiated directly.")


class ABCLayer(ABC):

    @abstractmethod
    def __init__(self):
        raise error

    @abstractmethod
    def __call__(self):
        raise error
