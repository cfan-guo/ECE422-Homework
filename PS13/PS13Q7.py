# Question 7
from math import *

c = 3e8
R_earth = 6378e3 # m
mu = 3.986e14 # blargh
k = 1.38064852*10**-23 # Boltzmann Const
To = 290

f = 10e9
wavelen = c/f

R = 100

L_3dB = 6
F_3dB = 2
L_3 = 10**(L_3dB/10.0)
F_3 = 10**(F_3dB/10.0)

T_2 = 350

L_1dB = 1
L_1 = 10**(L_1dB/10.0)

G_adB = 10
G_a = 10**(G_adB/10.0)
T_a = 280

# Part a
print("\nPart a)")
v_maxKM = -200
v_maxMS = v_maxKM*1000/(60.0*60)

delta_f = -2.0*f*(v_maxMS/c)
f_sig = delta_f+f
print("Delta f: "+str(delta_f)+" Hz")
print("Signal freq: "+str(f_sig)+" Hz")

B = delta_f
N = k*T_a*B #don't multiply in the gain
N_dB = 10*log(N, 10)
print("Noise power: "+str(N_dB)+"[dB]")

# Part b
print("\nPart b)")
Wt = 214e-3
A_eff = G_a*wavelen**2/(4*pi)
Dia = 7.4e-2
RCS = pi*(Dia/2)**2
Wr = A_eff*RCS*G_a*Wt/(4*pi*R**2)**2

SNR = Wr/N
SNR_dB = 10*log(SNR, 10)
print("Wr: "+str(Wr))
print("Ni: "+str(N))
print("SNR: "+str(SNR))
print("SNR: "+str(SNR_dB)+"[dB]")

# Part c
print("\nPart c)")
SNR_mindB = 10 #dB
SNR_min = 10**(SNR_mindB/10.0)

# F = SNR_in/SNR_out = 1+T_cas/To
# T_cas = T_a(SNR_in/SNR_out - 1)
T_cas = T_a*(SNR/SNR_min - 1)

# T_cas = (L_1-1)*290 + T_2*L_1 + (F_3-1)*290*L_1/G
# T_casp is first part of T_cas
# T_3p is the other multiplied stuff on top of G
T_casp = (L_1-1)*290 + T_2*L_1
T_3p = (F_3-1)*290*L_1

G =  T_3p/(T_cas - T_casp) #T_casp, T_3p match whatever is in the soln
print("G: " + str(G))

