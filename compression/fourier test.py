import numpy as np
import matplotlib.pyplot as plt


freqs = [100,0] #frequencies
amps  = [1,1] #amplitudes of corresponding freqs

#fs = 2*max(freqs)+100 #sample freq
fs = 20000

tstep = 1/fs #time step
n = max(freqs)+100
#n = int(fs/(min(freqs))) #number of samples

t = np.linspace(0,(n-1)*tstep,n) #time steps
fstep = fs/n #freq interval
#x axis for freqs
f = np.linspace(0,(n-1)*fstep,n)

#y = 1*np.sin(2*np.pi*f0*t)+0.25*np.sin(2*np.pi*f1*t)
y = sum([amps[i]*np.sin(2*np.pi*freqs[i]*t) for i in range(len(freqs))])

#print(y)


x = np.fft.fft(y)
xmag = np.abs(x)/n


fig,[ax1,ax2] = plt.subplots(nrows=2,ncols=1)

fplot = f[0:int(n/2+1)]
xmagplot = 2*xmag[0:int(n/2+1)]
xmagplot[0] /= 2
xmagplot = np.round(xmagplot,2)

print(*fplot,sep="\t")
print(*xmagplot,sep="\t")
ax1.plot(t,y,'.-')
ax2.plot(fplot,xmagplot,'.-')
plt.show()





'''
fs/f0 must be >2 for perfect signal recreation

'''