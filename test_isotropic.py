__author__ = 'Pavel Dmitriev'

import numpy as np
import matplotlib.pyplot as plt
from isotropicTransferMatrix import *
from transferMatrix import solve_transfer_matrix
import pytmm.transferMatrix as tm

c = 299792458  # m/c

ran_w = np.linspace(50, 1200, 100, endpoint=False)
ran_w = np.multiply(ran_w, 10 ** 12) # (1/(2*np.pi))*
ran_l = np.divide(c, ran_w)

eps_1 = 2.25
n_1 = np.sqrt(eps_1)

n_2 = np.sqrt(n_1)
eps_2 = n_2**2

kx = 0
ky = 0

d_nm = 600 / (n_2 * 4) # quarter-wavelength coating
d_m = d_nm * 10**-9

refl0 = []
refl = []
for i in ran_l:
    # substrate layer (considered infinite, so only bounding layer needed)
    a = tm.TransferMatrix.boundingLayer(1, n_1)

    R, T = tm.solvePropagation(a)
    refl0.append(np.abs(R**2))

    # antireflective layer layer "left" of substrate
    b = tm.TransferMatrix.layer(n_2, d_nm, i*10**9)
    a.appendRight(b)

    R, T = tm.solvePropagation(a)
    refl.append(np.abs(R**2))

a_refl = []
a_refl0 = []
for w in ran_w:
    #kx = c/(np.sqrt(2)*w)
    kx = 0
    D = build_isotropic_layer_matrix(eps_2, w, kx, ky, d_m)
    D_b = build_isotropic_bounding_layer_matrix(eps_1, w, kx, ky, d_m)

    r_ss, r_sp, r_ps, r_pp, t_ss, t_sp, t_ps, t_pp = solve_transfer_matrix(numpy.dot(D_b, D))
    a_refl.append(np.abs(r_pp**2))

    r_ss, r_sp, r_ps, r_pp, t_ss, t_sp, t_ps, t_pp = solve_transfer_matrix(D_b)
    a_refl0.append(np.abs(r_pp**2))



#PyATMM
plt.plot(ran_l*10**9, a_refl0)
plt.plot(ran_l*10**9, a_refl)

#PyTMM
plt.plot(ran_l*10**9, refl0, 'o')
plt.plot(ran_l*10**9, refl, 'o')


plt.xlabel("Wavelength, nm")
plt.ylabel("Reflectance")
plt.title("Reflectance of ideal single-layer antireflective coating")
plt.legend(['ATMM', 'ATMM', 'TMM', 'TMM'], loc='best')
plt.show(block=True)