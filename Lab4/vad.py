#Libraries
from pylab import *
from scipy.io import wavfile

#Processing the data
fs, data = wavfile.read("dk_tch_i.wav")
data = data[:,0]

##Short Energy
#dh - 7k sp - 1k
lenw = 7000

#Create energy values
ham = np.hamming(lenw)
nx = int(len(data)/lenw)
ny = len(data)
win = np.zeros((nx,ny))
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
#print(scleng)

#Plot data
plt.plot(data)
plt.plot(5000*engvad)
plt.title("VAD using short energy")
plt.xlabel("time")
plt.ylabel("Signal strength")
plt.axis("off")
plt.show()

##Short zero crossings
#Find zero diff between x(n) and x(n-1)
bigdata = list(data)*nx
bigdata = array(bigdata).reshape(nx,len(data))
crss = bigdata*win
minu = sign(crss)
minu = minu.T
minu = minu[:-1]
temp = np.zeros(shape(crss.T))
temp[1:] = minu
temp[0] = np.zeros(size(minu[0]))
minu = list(np.zeros(size(minu[0]))) + list(minu)
minu = array(temp).T
zrcrss = abs(sign(crss)-minu)
#Obtain the zero crossings by summing
nzc = sum(zrcrss,axis = 1)
#print(nzc)
nzc_thres = 560
boolnzc = np.less(nzc,nzc_thres*np.ones(len(nzc)))
nzcvad = list(boolnzc)*lenw
nzcvad = array(nzcvad).reshape(lenw,len(nzc))
nzcvad = nzcvad.T
nzcvad = nzcvad.reshape(int(lenw*len(nzc)),1)

#Plot data
plt.plot(data)
plt.plot(5000*nzcvad)
plt.title("VAD using zero crossings")
plt.xlabel("time")
plt.ylabel("Signal strength")
plt.axis("off")
plt.show()
