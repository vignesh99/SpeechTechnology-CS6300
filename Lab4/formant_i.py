#Libraries
from pylab import *
from scipy.io import wavfile
from scipy.signal import find_peaks
from scipy import signal

#Processing the data
fs, data = wavfile.read("ee.wav")
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
#print(x)
#print(y)

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
#Test plots
#plt.plot(w[1:],isig[100])
#plt.show()

#Cepstrum analysis
hlift = 80
lwin = np.zeros(shape(isig))
lwin[:,:hlift] = 1
envcp = isig*lwin
env = fft(envcp,48000, axis = 1) 
env = ifftshift(np.log(env),axes = 1)
#env[100] = fft(envcp[100],48000)

#Test plots
#plt.plot(w,env[100])
#plt.show()
formant = np.zeros((len(env),2))
#print(shape(formant))
for i in range(0,len(env)) :
    peaks, _ = find_peaks(env[i])
    mid = len(peaks)//2
    #print(i,peaks[mid])
    formant[i][0] = peaks[mid]
    formant[i][1] = peaks[mid+1]
    
formant = formant.T
#print(formant)
ffrm1 = w[formant[0].astype(int)]
ffrm2 = w[formant[1].astype(int)]

#plot the formants
#f, t, Sxx = signal.spectrogram(data, 48000)
#plt.pcolormesh(t, f, Sxx)
plt.plot(ffrm1,label = "1st formant")
plt.plot(ffrm2,label = "2nd formant")
plt.legend()
plt.title("Formant contour of /i/")
plt.xlabel("time")
plt.ylabel("frequency")
plt.xlim(60,135)
plt.ylim(0,10000)
plt.show()
print(average(ffrm1),average(ffrm2))
