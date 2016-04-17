# Question 2
from math import *

c = 3e8
R_earth = 6378e3 # m
mu = 3.986e14 # blargh
k = 1.38064852*10**-23 # Boltzmann Const

f = 20e9
arc_h = 10
arc_v = 5
BW_range = 250 # m

#Part a) aperture antenna dim, gain
# HPBW = lambda/current distro

print("Part a) aperture antenna dim, gain")
wavelen = c/f

BW_h = 10/250.0 
BW_v = 5/250.0
d_h = wavelen/BW_h
d_v = wavelen/BW_v

A_eff = d_h*d_v
G = 4*pi/(BW_h*BW_v)

print("Hori length: "+str(d_h)+"m")
print("Verti length: "+str(d_v)+"m")
print("A_eff: "+str(A_eff)+"m^2")
print("Gain: "+str(G))

#Part b) what is required transmit power?
print("\nPart b) req'd transmit power")
RCS = 1 # m^2
R_ob = 300 # 300 m away
SNR_dB = 30 # dB
SNR = 10**(SNR_dB/10.0)
T_sys = 1200 #k
B = 5e6 #Hz

Wr = SNR*k*T_sys*B
Wt = (Wr*(4*pi*R_ob**2)**2)/(A_eff*G*RCS)
print("Wt: "+str(Wt)+"W")

#Part c)
print("\nPart c) Doppler shift")
v_clear = 9 # m/s
delta_f = -2*f*v_clear/c
print("Freq shift: "+str(delta_f)+"Hz")

#Part d)
print("\nPart d) PRF")
min_range = 600 #m
t_r = 2*min_range/c
PRF = 1/t_r
print("PRF: "+str(PRF)+"Hz")
