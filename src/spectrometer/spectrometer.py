from .specter import Specter


from abc import ABC,abstractmethod
import numpy as np

import seabreeze
seabreeze.use('pyseabreeze')

class Spectrometer(ABC):
    @abstractmethod
    def set_integration_time(self,integration_time:int)->None:pass

    @abstractmethod
    def read(self)->Specter:pass

