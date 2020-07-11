#Libraries
from pylab import *
from scipy.io import wavfile

#Processing the data
fs, data = wavfile.read("dk_k_i.wav")
data = data[:,0]

##Short Energy
#dh - 7k sp - 1k
lenw = 7000

#Create energy values
ham = np.hamming(lenw)
nx = int(len(data)/lenw)
ny = len(data)
win = np.zeros((nx,ny))
scam = 5.824*np.ones((nx,ny))
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
bigdata = list(abs(data))*nx
bigdata = array(bigdata).reshape(nx,len(data))
eng = bigdata*win
scleng = sum(eng,axis = 1)
#7L works
eng_thres = 700000
booleng = np.greater(scleng,eng_thres*np.ones(len(scleng)))
engvad = list(booleng)*lenw
engvad = array(engvad).reshape(lenw,len(scleng))
engvad = engvad.T
engvad = engvad.reshape(int(lenw*len(scleng)),1)

print(booleng)
w = linspace(-24000,24000,48000)
i=0
ptime = np.zeros(nx)
for i in range(0,len(booleng)) :
    if(booleng[i] != 0 and i < nx and i!=8 and i!=9) :
        print("HI")
        print(i)
        signal = data*win[i]
        #plt.plot(data)
        #plt.plot(5000*win[i])
        #plt.show()
        fsig = fft(signal,48000)
        #plt.plot(w,fsig)
        #plt.show()
        msig = (abs(fsig))**2
        check = np.where(msig != 0)[0]
        print(check)
        msig = msig[check]
        #print(np.where(msig==0)[0],"CHECK")
        lsig = np.log(msig)
        #lmin = min(lsig)
        #lsig = lsig/lmin
        isig = ifft(lsig,48000)
        hlift = 40
        isig = ifftshift(isig[1:])
        #plt.plot(w[1:],isig)
        #plt.show()
        hwin = np.ones(len(isig))
        hwin[len(hwin)//2 - hlift : len(hwin)//2 + hlift] = np.zeros(2*hlift)
        pitch = hwin*isig 
        #plt.plot(w[1:],pitch)
        #plt.show()
        pwin = np.zeros(len(pitch))
        pwin[np.where(w > 0)[0][0] : np.where(w < 401)[0][-1]] = 1
        pitch = pitch*pwin
        #plt.plot(abs(pitch))
        #plt.show()
        pmax = np.where(abs(pitch) == max(abs(pitch)))[0]
        #print(pmax,pitch[pmax])
        pfreq = w[pmax]
        ptime[i] = 1/pfreq
        i = i+1
        
    else :
        continue

plt.plot(ptime)
plt.show()




'''
lz = len(np.where(engvad == 0)[0])
newdata = data*engvad
newdata = newdata + scam
cldata = newdata[np.where(newdata!=5.824)[0]]
cldata = cldata.reshape(nx,
'''
