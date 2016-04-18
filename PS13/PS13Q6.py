# Question 6
from math import *

c = 3e8
R_earth = 6378e3 # m
mu = 3.986e14 # blargh
k = 1.38064852*10**-23 # Boltzmann Const

f = 79e6
Wt = 106.9e3
h_t = 491 # m
v_km = -100
v_ms = v_km*1000/(60*60)
R_1 = 40e3
R_2 = 500
T_a = 170
F_dB = 10
F = 10**(1)
B = 6e6
Gt_dB = 2.15
Gt = 10**(Gt_dB/10)

wavelen = c/f

# Part a
print("\nPart a)")
RCS = 1
D_1 = sqrt(h_t**2 + R_1**2)
Pr = Gt*Wt/(4*pi*R_2**2)*RCS/(4*pi*D_2**2)
print("Rx power density: "+str(Pr)+" W/m^2")

# Part b
print("\nPart b)")
Gr_dB = 12 #dBi
Gr = 10**(Gr_dB/10.0)
delta_f = -2*f*(v_ms/c)
f_car = f+delta_f

T_r = (F-1)*290
T_sys = T_a + T_r

A_eff = Gr*wavelen**2/(4*pi)
Wr = A_eff*Pr
N = k*T_sys*B
CNR = Wr/N
CNR_dB = 10*log(CNR, 10)

print("Perceived f: "+str(f_car)+" Hz")
print("CNR: "+str(CNR_dB)+" [dB]")

# Part c
print("\nPart c)")
CNR_need = 20 #dB
M = 6
G_need = CNR_need + M - CNR_dB + Gr_dB
print("Needed gain: "+str(G_need)+" [dB]")

# Part d
print("\nPart d)")
A_plate = sqrt(RCS*wavelen**2/(4*pi))
print("Flat plate area: "+str(A_plate)+" m^2")

# Part e
print("\nPart e)")
