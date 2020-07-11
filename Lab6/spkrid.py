#Libraries
from pylab import *
from scipy.io import wavfile

#Obtain Cepstrum
def stdCeps(data, lenw = 1000,Ndft = 256) :
    ##Short Energy
    #Create energy values
    ham = np.hamming(lenw)
    nx = int(len(data)/lenw)
    ny = len(data)
    win = np.zeros((nx,ny))
    scam = 10.676*np.ones((nx,ny))
    #x-coordinate array
    x = np.arange(0,nx)
    x = list(x)*lenw
    x = array(x).reshape(lenw,nx)
    x = x.T
    #y-coordinate array
    y = np.arange(0,lenw)
    y = list(y)*nx
    y = array(y).reshape(nx,lenw)
    const = lenw*x
    y = y + const

    #Moving window generation
    win[x,y] = ham
    scam[x,y] = 0
        
    #Find energy at different windows
    bigdata = list(data)*nx
    bigdata = array(bigdata).reshape(nx,len(data))
    dwin = bigdata*win
    dwin = dwin + scam
    eng = dwin[np.where(dwin!=10.676)]
    eng = eng.reshape((nx,lenw))

    #Frequency analysis of data
    w = linspace(-Ndft//2,Ndft//2,Ndft)
    fsig = fft(eng,Ndft,axis = 1)
    msig = (abs(fsig))**2
    lsig = np.log(msig)
    lmin = amin(lsig,axis = 1)
    lmin = repeat(lmin,len(lsig[0]))
    lmin = lmin.reshape(shape(lsig))
    lsig = lsig
    isig = ifft(lsig,Ndft,axis = 1)
    isig = isig[:,1:]
    #Test plots
    #plt.plot(w[1:],isig[3])
    #plt.show()
    
    #Return Cepstrum value
    return isig

#Processing the data
######Train data cepstrum#######
#Sampled at 16k single channel
database = []
#Group 1
fs, data = wavfile.read("1_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("1_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("1_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("1_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("1_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("1_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 3
fs, data = wavfile.read("3_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("3_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("3_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("3_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("3_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("3_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 4
fs, data = wavfile.read("4_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("4_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("4_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("4_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("4_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("4_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 6
fs, data = wavfile.read("6_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("6_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("6_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("6_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("6_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("6_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 7
fs, data = wavfile.read("7_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("7_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("7_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("7_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("7_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("7_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 8
fs, data = wavfile.read("8_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("8_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("8_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("8_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("8_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("8_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 9
fs, data = wavfile.read("9_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("9_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("9_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("9_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("9_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("9_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 13
fs, data = wavfile.read("13_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("13_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("13_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 15
fs, data = wavfile.read("15_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("15_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("15_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("15_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("15_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("15_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 16
fs, data = wavfile.read("16_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("16_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("16_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("16_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("16_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("16_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 18
fs, data = wavfile.read("18_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("18_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("18_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("18_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("18_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("18_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

#Group 19
fs, data = wavfile.read("19_1/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("19_1/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("19_1/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("19_2/1.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("19_2/2.wav")
ceps = stdCeps(data = data)
database.append(ceps)

fs, data = wavfile.read("19_2/3.wav")
ceps = stdCeps(data = data)
database.append(ceps)

database = array(database)
print(shape(database[5]),shape(database[9]))


########Test data Cepstrum######
testdata = []
#Group 1
fs, data = wavfile.read("1_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("1_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("1_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("1_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 3
fs, data = wavfile.read("3_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("3_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("3_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("3_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 4
fs, data = wavfile.read("4_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("4_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("4_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("4_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 6
fs, data = wavfile.read("6_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("6_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("6_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("6_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 7
fs, data = wavfile.read("7_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("7_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("7_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("7_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 8
fs, data = wavfile.read("8_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("8_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("8_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("8_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 9
fs, data = wavfile.read("9_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("9_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("9_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("9_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 13
fs, data = wavfile.read("13_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("13_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 15
fs, data = wavfile.read("15_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("15_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("15_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("15_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 16
fs, data = wavfile.read("16_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("16_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("16_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("16_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 18
fs, data = wavfile.read("18_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("18_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("18_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("18_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

#Group 19
fs, data = wavfile.read("19_1/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("19_1/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)

fs, data = wavfile.read("19_2/4.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)
data1 = data

fs, data = wavfile.read("19_2/5.wav")
ceps = stdCeps(data = data)
testdata.append(ceps)
data2 = data

#Labels for training data
trainLabel = repeat(np.arange(12),6)
#print(trainLabel)

#Labels for test data
testLabel = repeat(np.arange(12),4)
#print(testLabel)

'''
Once you find min(cost) among all the 69 do ind = np.where(cost_vector)[0]
after you get the index just do trainLabel(ind)
you will get the speaker ID
compare this with trainLabel

'''
Ndft = 256
w = linspace(-Ndft//2,Ndft//2,Ndft)
#Report plots
#Check data plots
plt.plot(data1,"r-")
plt.plot(data2)
plt.xlabel("time")
plt.ylabel("Signal strength")
plt.title("Time domain speech signal of same speaker")
plt.show()

plt.plot(w[1:],abs(database[2][3]),label = "train")
plt.plot(w[1:],abs(testdata[1][3]),label = "test")
plt.title("Comparison of cepstrum with same sentence same speaker")
plt.xlabel("qfreq")
plt.ylabel("Magnitude")
plt.legend()
plt.show()

plt.plot(w[1:],abs(database[4][3]),label = "train")
plt.plot(w[1:],abs(testdata[1][3]),label = "test")
plt.title("Comparison of cepstrum with same sentence different speaker")
plt.xlabel("qfreq")
plt.ylabel("Magnitude")
plt.legend()
plt.show()

plt.plot(w[1:],abs(database[8][3]),label = "train")
plt.plot(w[1:],abs(testdata[1][3]),label = "test")
plt.title("Comparison of cepstrum with different sentence different speaker")
plt.xlabel("qfreq")
plt.ylabel("Magnitude")
plt.legend()
plt.show()

