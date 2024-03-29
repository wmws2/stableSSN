import numpy as np
import matplotlib.pyplot as plt
import os
import time
import scipy.io
from mpmath import *
mp.dps = 100

folder = 'rebuttal/'
C = np.load(folder+'feature_C_norm.npy')
A = np.load(folder+'filter_bank_norm.npy').reshape(50,32*32).T
sigma_x = np.load(folder+'noise_std.npy')
AT = A.T
ATA = matrix(AT@A)
ACAT = matrix(A@C@AT)

print("Computing inverse...")
C = matrix(C)
Cinv = C**-1
print("Done!")

Nz = 500
z_axis = np.linspace(0.01,1.5,Nz)

covs = np.zeros([500,50,50])
for z in range(Nz):
	print(z)
	#cholesky(mpmathify(z_axis[z]**2) * ACAT + mpmathify(sigma_x**2) * eye(32*32))
	covs[z] = np.array(((Cinv +  mpmathify(z_axis[z]**2/(sigma_x**2)) * ATA)**-1).tolist(),dtype=np.float32)

np.save(folder+'mpcovs.npy',covs)
#(z_axis[z])**2 * ACAT + sigma_x**2 * np.identity(32*32) #need cholesky for this
#Cinv +  (z_axis[z])**2/(sigma_x**2) * ATA #need cov for this
