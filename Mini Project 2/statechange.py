                                    #Import libraries
from pylab import *
import os

for subdir, dirs, files in os.walk("ctsModels"):
    dirname = subdir.split(os.path.sep)[-1]
    print('Directory:', dirname)
    if dirname == "2 digit":
        for f in files:
                                    #Change the state
                files = open("ctsModels/2 digit/"+f,"r")
                lines = files.readlines()
                print(lines[0])
                lines[0] = "states: 10\n"
                files.close()
                
                files = open("ctsModels/2 digit/"+f,"w")
                files.writelines(lines)
                files.close()
                
                files = open("ctsModels/2 digit/"+f,"r")
                lines = files.readlines()
                print(lines[0])
                files.close()
