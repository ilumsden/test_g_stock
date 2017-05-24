import numpy as npy
import matplotlib.pyplot as mpyplot
#import yahoo_finance as yf

google = npy.loadtxt(fname="GOOGL2.csv", delimiter=",")

fig = mpyplot.figure(figsize=(10.0, 3.0))

h_data = google[:,1]
l_data = google[:,2]
c_data = google[:,3]

axes1 = fig.add_subplot(4, 1, 1)
axes2 = fig.add_subplot(4, 1, 2)
axes3 = fig.add_subplot(4, 1, 3)

axes1.set_ylabel("Daily High Share Prices")
axes1.plot(h_data)

axes2.set_ylabel("Daily Low Share Prices")
axes2.plot(l_data)

axes3.set_ylabel("Daily Closing Share Prices")
axes3.plot(c_data)

fig.tight_layout()

mpyplot.show()




