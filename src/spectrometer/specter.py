import numpy as np
class Specter:
    def __init__(self,wavelengths:np.ndarray,intensities:np.ndarray) -> None:
        self.wavelengths=wavelengths
        self.intensities=intensities
