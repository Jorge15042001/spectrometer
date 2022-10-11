from .spectrometer import Spectrometer
from .specter import Specter

import numpy as np

import seatease.spectrometers as s

class testSpectrometer(Spectrometer):
    def __init__(self,integration_time:int=100000) -> None:
        super().__init__()
        self.integration_time:int = integration_time
        self.device:s.Spectrometer = s.Spectrometer.from_first_available()

    def set_integration_time(self, integration_time: int)->None:
        self.integration_time = integration_time
        self.device.integration_time_micros(self.integration_time) # 10 ms

    def read(self) -> Specter:
        wavelengths = self.device.wavelengths()
        intensities = self.device.intensities()
        return Specter(wavelengths,intensities)
