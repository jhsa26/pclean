#!/usr/bin/env python

import matplotlib.pyplot as plt
import scipy
#Will demostrate the conv function

u = [1,2,3,4,5,4,3,2,1]
v = [1,3,5,7,9,6,4,2,3,7]

plt.subplot(311)
plt.stem(u)
plt.title('Input sequence')


plt.subplot(312)
plt.stem(v)
plt.title('Impulse Response')

w = scipy.convolve(u,v)
plt.subplot(313)
plt.stem(w)
plt.title('Convolve U * V')

plt.show()
