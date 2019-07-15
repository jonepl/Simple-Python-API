from abc import ABC, abstractmethod

class Controller(ABC):

    def __init__(self):
        super(AbstractOperation, self).__init__()

    @abstractmethod
    def listResources(self):
        """
        Returns collection of resources as a python dictionary
        """
        raise NotImplementedException
    
    @abstractmethod
    def runResource(self, resource):
        """
        Returns a resources as a python dictionary
        """
        raise NotImplementedException