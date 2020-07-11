
#Import libraries
from pylab import *
import pandas as pd

v = pd.read_csv("sa1F.csv",header = None)

#Create lists out of CSV files
#aa
aaf1 = v[0].values
aaf2 = v[1].values
eef1 = v[2].values
eef2 = v[3].values
uuf1 = v[4].values
uuf2 = v[5].values
aef1 = v[6].values
aef2 = v[7].values
oof1 = v[8].values
oof2 = v[9].values

#plots
plt.scatter(aaf1,aaf2, label = "aa")
plt.scatter(eef1,eef2, label = "ee")
plt.scatter(uuf1,uuf2, label = "uu")
plt.scatter(aef1,aef2, label = "ae")
plt.scatter(oof1,oof2, label = "oo")
plt.title("Vowel Triangle Female Source")
xlabel("1st formant")
ylabel("2nd formant")
plt.legend()
plt.show()

v = pd.read_csv("sa1M.csv",header = None)

#Create lists out of CSV files
#aa
aaf1 = v[0].values
aaf2 = v[1].values
eef1 = v[2].values
eef2 = v[3].values
uuf1 = v[4].values
uuf2 = v[5].values
aef1 = v[6].values
aef2 = v[7].values
oof1 = v[8].values
oof2 = v[9].values

#plots
plt.scatter(aaf1,aaf2, label = "aa")
plt.scatter(eef1,eef2, label = "ee")
plt.scatter(uuf1,uuf2, label = "uu")
plt.scatter(aef1,aef2, label = "ae")
plt.scatter(oof1,oof2, label = "oo")
plt.title("Vowel Triangle Male source")
xlabel("1st formant")
ylabel("2nd formant")
plt.legend()
plt.show()

