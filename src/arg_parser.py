import argparse 

def bool_none(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    return None


"""
python main.py 
    devices
        --list
        --information
    calibrate
        --list-calibrations
        --device: str
        --output: calibrationFile
        --strategy:str b&w
    run 
        --config-file
        --integration-time
        --device
        --save
        --save-format
"""


parser:argparse.ArgumentParser = argparse.ArgumentParser(description= 'Spectrometer command line interface')

subparsers = parser.add_subparsers(title="spectrometer commands",dest="command")

devicesParser:argparse.ArgumentParser = subparsers.add_parser("devices",aliases=['d'],description="manage available spectrometers",help="manage available spectrometers")
devicesParser.add_argument('-l','--list', action='store_true',  help='list all available devices')
devicesParser.add_argument('-i','--information', action='store_true',  help='query information about spectrometer')



runParser:argparse.ArgumentParser = subparsers.add_parser("run", aliases=['r'],description="run spectrometer",help="run spectrometer")

runParser.add_argument('-c','--config-file', type=str, default="config/example_config.json",  help='run with specific config file')
runParser.add_argument('-i','--integration-time', type=int,  help='run spectrometer with specific integration time')
runParser.add_argument('-d','--device', type=str,   help='connect to an specific sensor')
runParser.add_argument('-s','--save', type=bool_none, default="" ,  help='save measurement')
#  runParser.add_argument('-s','--save',action="store_true", help='save measurement')
runParser.add_argument('-f','--save-format', type=str,   help='format to save the measurement')



calibrationParser:argparse.ArgumentParser = subparsers.add_parser("calibrate",aliases=['c'],description="calibrate spectrometer",help="calibrate spectromemter")

calibrationParser.add_argument('-l','--list-calibrations',action='store_true',help="list all available calibrations")
calibrationParser.add_argument('-d','--device', type=str,  default='any', help='calibrate specific device')
calibrationParser.add_argument('-o','--output', type=str,  default='default', help='name of calibration file')
calibrationParser.add_argument('-s','--strategy', type=str,  default='b&w', help='calibration strategy')
