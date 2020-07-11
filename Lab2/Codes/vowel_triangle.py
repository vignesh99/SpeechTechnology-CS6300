#Import libraries
from pylab import *
import csv

#Create lists out of CSV files
#aa
aaf1 = []
aaf2 = []
with open("aa.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        aaf1.append(row[:1])
        aaf2.append(row[1:2])

#ee
eef1 = []
eef2 = []
with open("ee.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        eef1.append(row[:1])
        eef2.append(row[1:2])
        
#uu
uuf1 = []
uuf2 = []
with open("uu.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        uuf1.append(row[:1])
        uuf2.append(row[1:2])
       
#ae
aef1 = []
aef2 = []
with open("ae.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        aef1.append(row[:1])
        aef2.append(row[1:2])

#oo
oof1 = []
oof2 = []
with open("oo.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        oof1.append(row[:1])
        oof2.append(row[1:2])
                         
#plots
plt.scatter(aaf1,aaf2, label = "aa")
plt.scatter(eef1,eef2, label = "ee")
plt.scatter(uuf1,uuf2, label = "uu")
plt.scatter(aef1,aef2, label = "ae")
plt.scatter(oof1,oof2, label = "oo")
plt.title("Vowel Triangle")
plt.legend()
plt.show()
