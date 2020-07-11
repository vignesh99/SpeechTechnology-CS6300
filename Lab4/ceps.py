#Libraries
from pylab import *
from scipy.io import wavfile
from scipy.signal import find_peaks

#Processing the data
fs, data = wavfile.read("ee.wav")
lsig = 1000
#print(shape(data))
data = data[:,0]
signal = data[int(len(data)/2)-5000 : int(len(data)/2) -5000 + lsig]

#Frequency analysis of data
fsig = fft(signal,48000)
msig = (abs(fsig))**2
lsig = np.log(msig)
lmin = min(lsig)
lsig = lsig/lmin
isig = ifft(lsig,48000)
w = linspace(-len(lsig)/2,len(lsig)/2,len(lsig))

#Envelope extraction using cepstrum
#For aa:40 ee:80
hlift = 80
envcp = array(list(isig[1:hlift+1]) + list(np.zeros(len(isig)-hlift)))
env = fft(envcp,48000) 
env = ifftshift(np.log(env))

#Pitch extraction
hlift = 80
isig = ifftshift(isig[1:])
hwin = np.ones(len(isig))
hwin[len(hwin)//2 - hlift : len(hwin)//2 + hlift] = np.zeros(2*hlift)
pitch = hwin*isig 
pwin = np.zeros(len(pitch))
pwin[np.where(w > -401)[0][0] : np.where(w < 401)[0][-1]] = 1
pitch = pitch*pwin
#pitch = array(list(np.zeros(hlift)) + list(isig[hlift : ]))
#pitch = fft(pitchcp,48000)
#pitch = ifftshift(np.log(pitch))

#Find peaks
peaks, _ = find_peaks(env)
#formant = [peaks[15],peaks[16],peaks[17],peaks[18]]
mid = len(peaks)//2
print(peaks[mid])
print(len(lsig))
formant = [peaks[mid-2],peaks[mid-1],peaks[mid],peaks[mid+1]]
#Plots
plt.plot(w,ifftshift(lsig))
plt.plot(w,env+4)
plt.plot(w[peaks],env[peaks]+4,"x")
plt.plot(w[formant],env[formant]+4,"ro")
plt.title("Formant detection using cepstrum for /i/")
plt.xlabel("freq")
plt.ylabel("Signal strength")
plt.show()

#Print formant values
print("The firsts and second formants are",w[formant][2:])

plt.plot(w[1:],abs(pitch))
plt.title("Pitch detection using cepstrum for /i/")
plt.xlabel("freq")
plt.ylabel("Signal strength")
plt.xlim(-500,500)
plt.show()

#Print pitch values
pfreq = linspace(-len(lsig)/2,len(lsig)/2,len(lsig))[np.where(pitch == max(pitch))[0]]
pfreq = abs(pfreq)
pperiod = 1/pfreq
print("pitch freq = ",pfreq,"pitch period = ",pperiod)

#plt.plot(w[1:],pwin)
#plt.plot(linspace(-len(lsig)/2,len(lsig)/2,len(lsig))[1:],isig,"x")
#plt.plot(linspace(-len(lsig)/2,len(lsig)/2,len(lsig))[peaks],env[peaks]+4,"x")
#print(np.where(env == max(env))[0])
#print(np.where(pitch == max(pitch))[0])
#print(np.where(w > -401)[0])
print(len(peaks))

