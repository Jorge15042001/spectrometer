from .spectrometer import Spectrometer
from .specter import Specter


import seabreeze
seabreeze.use('pyseabreeze')
import seabreeze.spectrometers as sbs

class PhysicalSpectrometer(Spectrometer):
    def __init__(self,device:sbs.Spectrometer,integration_time:int=100000) -> None:
        super().__init__()
        self.integration_time:int = integration_time
        self.device:sbs.Spectrometer = device
        self.device.integration_time_micros(integration_time)

    def set_integration_time(self, integration_time: int)->None:
        self.integration_time = integration_time
        self.device.integration_time_micros(self.integration_time) # 10 ms

    def read(self) -> Specter:
        wavelengths = self.device.wavelengths()
        intensities = self.device.intensities()
        return Specter(wavelengths,intensities)
