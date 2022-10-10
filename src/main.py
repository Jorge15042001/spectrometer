import seabreeze
seabreeze.use('pyseabreeze')

from seabreeze.spectrometers import list_devices, Spectrometer

from datetime import datetime


fileName = datetime.utcnow().strftime('%F--%T.%f')[:-3]

spec = Spectrometer.from_first_available()
print(spec)

spec.integration_time_micros(100000)  # 0.1 seconds
wavelengths_raw = spec.wavelengths()
intensities_raw = spec.intensities()

## eliminar datos por debajo de 640
wavelengths = []
intensities = []

for i in range(len(wavelengths_raw)):
    if wavelengths_raw[i]<0: continue
    wavelengths.append(wavelengths_raw[i])
    intensities.append(intensities_raw[i])

dataFile = open("mediciones/"+fileName+".csv","w")
for i in range(len(wavelengths)):
    dataFile.write(str(wavelengths[i])+","+str(intensities[i])+"\n")

plt.plot(wavelengths, intensities)
plt.savefig("mediciones/"+fileName+".png")
plt.show()
