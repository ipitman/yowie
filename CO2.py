from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt

f = urlopen('ftp://ftp.ncdc.noaa.gov/pub/data/paleo/icecore/antarctica/domefuji/df-co2-wet-340ka-2007.txt')

with open('CO2_data.py', 'w') as d:
	for line in f.read().decode('utf-8').split('\n')[134:425]:
		d.write('{},{},{},{},{}\n'.format(line[:8].strip(), line[8:19].strip(), line[19:28].strip(), line[29:39].strip(), line[39:].strip()))

df = pd.read_csv('CO2_data.py')

s = df.set_index('GasAge')['CO2wet']
s.index = -s.index

plt.plot(s)
plt.ylabel('ppm of CO2')
plt.xlabel('years before present')

plt.show()
