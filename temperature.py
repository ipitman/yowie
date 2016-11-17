from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt

f = urlopen('ftp://ftp.ncdc.noaa.gov/pub/data/paleo/icecore/antarctica/domefuji/df-tsite-340ka-dfo2006.txt')

with open('temperature_data.py', 'w') as d:
	for line in f.read().decode('utf-8').split('\n')[142:822]:
		d.write('{},{},{}\n'.format(line[:6].strip(), line[6:18].strip(), line[18:27].strip()))

df = pd.read_csv('temperature_data.py')
s = df.set_index('CenterAge')['deltaT']
s.index = -s.index

plt.plot(s)
plt.ylabel('deviation from mean temperature')
plt.xlabel('years before present')

plt.show()