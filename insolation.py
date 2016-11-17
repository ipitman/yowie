from urllib.request import urlopen
import pandas as pd
import matplotlib.pyplot as plt

f = urlopen('ftp://ftp.ncdc.noaa.gov/pub/data/paleo/insolation/insol91.jun')

with open('insolation_data.py', 'w') as d:
	d.write('kya')
	for line in f.read().decode('utf-8').split('\n')[1:1004]:
		d.write('{},{},{},{}\n'.format(line[:6].strip(), line[6:14].strip(), line[14:22].strip(), line[22:30].strip()))

df = pd.read_csv('insolation_data.py')
s = df.set_index('kya')['90NJune']
s = s.loc[:-350]
s.index *= 1000

plt.plot(s)
plt.ylabel('solar insolation in watts per square meter')
plt.xlabel('years before present')

plt.show()