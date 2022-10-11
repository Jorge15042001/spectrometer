from spectrometer.specter import readFromCSV
from spectrometer.spectrometer_capturer import SpectrometerCapturer
#  #  from spectrometer.test_spectrometer import testSpectrometer
from spectrometer.calibrator import CalibraionrStrategy, NoCalibration,LineaerInterpolationCalibration
#
from arg_parser import parser

from datetime import datetime
import numpy as np
import json

if __name__ == "__main__":
    arguments = parser.parse_args()
    if  arguments.command=='r' or arguments.command =='run':
        json_file = open(arguments.config_file)
        configuration = json.load(json_file)
        device:str = arguments.device if arguments.device else configuration["device"]
        integration_time:int = arguments.integration_time if arguments.integration_time else configuration['integration_time_us']
        export:bool = arguments.save if arguments.save else configuration["export_options"]["export"]
        export_strategy:str = arguments.save_format if arguments.save_format else configuration["export_options"]["export_strategy"]
        export_format:str = configuration["export_options"]["filename_format"]
        
        calibrator:CalibraionrStrategy = LineaerInterpolationCalibration(readFromCSV("calibrations/white.csv"),readFromCSV("calibrations/black.csv"))
        #  calibrator:CalibraionrStrategy = NoCalibration()
        capturer:SpectrometerCapturer = SpectrometerCapturer(device,integration_time,export,export_strategy,export_format,calibrator)
        capturer.getSpecter()
    elif  arguments.command=='c' or arguments.command =='calibrate':
        pass   
