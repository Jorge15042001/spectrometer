import numpy as np
class Specter:
    def __init__(self,wavelengths:np.ndarray,intensities:np.ndarray) -> None:
        self.wavelengths=wavelengths
        self.intensities=intensities
def readFromCSV(filename:str)->Specter:
    f = open(filename)
    wavelengths:list[float] = []
    intensities:list[float] =[]
    for line in f.readlines():
        line = line.strip("\n")
        wave_str,inte_str = line.split(",")
        wave = float(wave_str)
        inte = float(inte_str)
        wavelengths.append(wave)
        intensities.append(inte)
    wavelengthsArray = np.array(wavelengths,float)
    intensitiesArray = np.array(intensities,float)
    return Specter(wavelengthsArray,intensitiesArray)
