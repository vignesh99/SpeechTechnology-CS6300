#Libraries
from pylab import *
from scipy.io import wavfile
from scipy.signal import find_peaks

#Processing the data
fs, data = wavfile.read("spf.wav")
data = data[:,0]

##Short Energy
#dh - 7k sp - 1k
lenw = 1000

#Create energy values
ham = np.hamming(lenw)
nx = int(len(data)/lenw)
ny = len(data)
win = np.zeros((nx,ny))
scam = 10.676*np.ones((nx,ny))
#x-coordinate arra
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
#print(x)
#print(y)

#Moving window generation
win[x,y] = ham
scam[x,y] = 0
#Find energy at different windows
bigdata = list(abs(data))*nx
bigdata = array(bigdata).reshape(nx,len(data))
eng = bigdata*win
scleng = sum(eng,axis = 1)
#7L works
eng_thres = 200000
booleng = np.greater(scleng,eng_thres*np.ones(len(scleng)))
engvad = list(booleng)*lenw
engvad = array(engvad).reshape(lenw,len(scleng))
engvad = engvad.T
engvad = engvad.reshape(int(lenw*len(scleng)),1)

#Find energy at different windows
bigdata = list(data)*nx
bigdata = array(bigdata).reshape(nx,len(data))
dwin = bigdata*win
dwin = dwin + scam
eng = dwin[np.where(dwin!=10.676)]
eng = eng.reshape((nx,lenw))

#Frequency analysis of data
w = linspace(-24000,24000,48000)
fsig = fft(eng,48000,axis = 1)
msig = (abs(fsig))**2
lsig = np.log(msig)
lmin = amin(lsig,axis = 1)
lmin = repeat(lmin,len(lsig[0]))
lmin = lmin.reshape(shape(lsig))
lsig = lsig
isig = ifft(lsig,48000,axis = 1)
isig = isig[:,1:]

#Cepstrum analysis
hlift = 80
hwin = np.ones(shape(isig))
hwin[:,:hlift] = 0
hwin[:,-hlift:] = 0
pitchcp = isig*hwin
#Test plots
#plt.plot(w[1:],pitchcp[100])
#plt.show()
#pitch = fft(pitchcp,48000, axis = 1) 
pitch = ifftshift(pitchcp,axes = 1)
#Test plots
#plt.plot(w[1:],abs(pitch[100]))
#plt.show()
pwin = np.zeros(shape(pitch))
pwin[:,np.where(w > 0)[0][0] : np.where(w < 401)[0][-1]] = 1
pitch = pitch*pwin
#Test plots
#plt.plot(w[1:],abs(pitch[100]))
#plt.show()
#print(amax(abs(pitch),axis = 1))
pmax = np.zeros(len(pitch))
maxval = amax(abs(pitch),axis = 1)
for i in range(0,len(pitch)) :
    pmax[i] = np.where(abs(pitch[i]) == maxval[i])[0]
    
#print(pmax)
pfreq = w[pmax.astype(int)]
#pfreq = repeat(pfreq,lenw)
#print(len(booleng),len(pfreq))
ptime = booleng*(1/pfreq)
#Plots
plt.plot(ptime)
plt.title("pitch period plot for female sentence")
plt.xlabel("time/observations")
plt.ylabel("pitch period")
plt.ylim(0,0.01)
plt.show()
print(average(ptime[np.where(ptime!=0)[0]]))

