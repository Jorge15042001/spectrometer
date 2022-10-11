from numpy import save
from .spectrometer import Spectrometer
from .test_spectrometer import testSpectrometer
from .spectrometer_physical import PhysicalSpectrometer,sbs
from .specter import Specter
from .calibrator import CalibraionrStrategy




from datetime import datetime
import numpy as np

def dontSave(a:Specter,filename_format:str)->None:
    pass

def saveAsCSV(spec:Specter,filename_format:str)->None:
    fileName = datetime.utcnow().strftime('%F--%T.%f')[:-3]

    dataFile = open("mediciones/"+fileName+".csv","w")
    for i in range(len(spec.wavelengths)):
        dataFile.write(str(spec.wavelengths[i])+","+str(spec.intensities[i])+"\n")
    dataFile.close()

def identity(x:Specter)->Specter:return x


def selectSpectrometer(device:str,integration_time:int)->Spectrometer:
    if device=="from_first_available":
        return PhysicalSpectrometer(sbs.Spectrometer.from_first_available(),integration_time) 
    elif device == "test":
        return testSpectrometer(integration_time)

    return testSpectrometer()
def selectSaveStrategy(export:bool,saveStrategy:str,filename_format:str):
    if not export:
        return lambda x:dontSave(x,"")
    if saveStrategy=="csv":
        return lambda x:saveAsCSV(x,filename_format)
    raise Exception("not a valid export strategy") 
    

class SpectrometerCapturer:
    def __init__(self,device:str,integration_time:int,export_measurement:bool,export_strategy:str,filename_format:str,calibrator:CalibraionrStrategy) -> None:

        self.spectrometer:Spectrometer = selectSpectrometer(device,integration_time) 
        self.calibrator = calibrator
        self.save = selectSaveStrategy(export_measurement,export_strategy,filename_format)



        ## selecting  spectrometer

        
    def getRawSpecter(self):
        spec = self.spectrometer.read()
        self.save(spec)
        return spec

    def getSpecter(self):
        spec = self.spectrometer.read()
        print(np.shape(spec.intensities))
        calibrated = self.calibrator.calibrate(spec)
        self.save(calibrated)
        return spec
