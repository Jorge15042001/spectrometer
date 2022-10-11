from abc import ABC,abstractmethod

from numpy.lib.index_tricks import nd_grid
from .specter import Specter

import numpy as np

#  def substractIntensities(s1:Specter,s2:Specter)->np.ndarray:
#      if np.shape(s1.wavelengths)[0]==np.shape(s2.wavelengths)[0]:return s1.intensities-s2.intensities
#
#      m_shape = (np.shape(s1.wavelengths)[0],np.shape(s2.wavelengths)[0])
#      m1 = np.array([s1.wavelengths]).transpose()
#      m1 = np.repeat(m1,m_shape[1],axis=1)
#
#      m2 = np.array([s2.wavelengths])
#      m2 = np.repeat(m2,m_shape[0],axis=0)
#
#      matrix_distance:np.ndarray = np.abs(m1-m2)
#
#      mins = np.argmin(matrix_distance,axis=np.argmin(m_shape))
#
#      biggest = s1.intensities
#      smallest = s2.intensities
#      if m_shape[0]<m_shape[1]:
#          biggest,smallest = smallest,biggest
#      print(biggest.shape)
#      print(smallest.shape)
#
#      result = np.zeros((biggest.shape[0]),float)
#      for i in range(len(result)):
#          result[i] = biggest[i] - smallest[mins[i]]
#
#      return result
#      it = 1

class CalibraionrStrategy(ABC):
    @abstractmethod
    def calibrate(self,spec:Specter)->Specter:pass

class LineaerInterpolationCalibration(CalibraionrStrategy):
    def __init__(self,white:Specter,black:Specter) -> None:
        super().__init__()
        self.white = white
        self.black = black
    def calibrate(self,spec:Specter)->Specter:
        
        calibrated_inten = (spec.intensities - self.black.intensities) / (self.white.intensities - self.black.intensities)
        #  calibrated_inten = substractIntensities(spec,self.black)/substractIntensities(self.white,self.black)
        calibrated:Specter = Specter(spec.wavelengths,calibrated_inten)
        return calibrated

class NoCalibration(CalibraionrStrategy):
    def __init__(self) -> None:
        super().__init__()
    def calibrate(self,spec:Specter)->Specter:
        return spec
