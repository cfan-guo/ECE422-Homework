# Question 5
from math import *

c = 3e8
R_earth = 6378e3 # m
mu = 3.986e14 # blargh
k = 1.38064852*10**-23 # Boltzmann Const

f = 18e9
G_dB = 20 #dBi
G = 10**(G_dB/10.0)
Wt = 100 #W

wavelen = c/f

# Part a
print("\nPart a)")
Wr = 0.280e-12
R = 1e3

A_eff = G*(wavelen**2)/(4*pi)
RCS = Wr*(4*pi*R**2)**2/(A_eff*G*Wt)
print("RCS: "+str(RCS)+" m^2")

# Part b
print("\nPart b)")
v_kmh = -140 #Km/H
v_ms = v_kmh*1000/(60*60.0)
delta_f = -2*f*v_ms/c
f_sig = delta_f + f
print("Delta f: "+str(delta_f)+" Hz")
print("Signal f: "+str(f_sig)+" Hz")

# Part c
print("\nPart c)")
T_rx = 2100 #k
T_ant = 400
B = 200e3 # 200KHz
CNR_reqdB = 10
CNR_req = 10**(CNR_reqdB/10.0)

T_sys = T_rx + T_ant
Wr = CNR_req*k*T_sys*B
A_eff = G*wavelen**2/(4*pi)
EIRP = Wt*G

R_max = sqrt(sqrt(A_eff*RCS*EIRP/Wr)/(4*pi))

print("Max range: "+str(R_max)+" m")

# Part d
print("\nPart d)")
l_ap = 20e-2
w_ap = 10e-2
A_effnew = l_ap*w_ap
G_new = A_effnew*4*pi/(wavelen**2)

EIRP_new = Wt*G_new

R_maxnew = sqrt(sqrt(A_effnew*RCS*EIRP_new/Wr)/(4*pi))
print("Max range: "+str(R_maxnew)+" m")

# Part e
print("\nPart e)")
W_rcardB = -50 #dBm
W_rcar = 10**((-50/10.0)-3)
G_rdB = 2.15 # dB
G_r = 10**(G_rdB/10.0)

A_effd = G_r*wavelen**2/(4*pi)
EIRP_car = Wt*G

R_car = sqrt(A_effd*EIRP_car/(4*pi*W_rcar))
v_km100 = 100
v_ms100 = v_km100*1000/(60*60.0)

t_slow = abs((R_car-R_max)/(v_ms100+v_ms))

print("R max of car: "+str(R_car)+" m")
print("Time to slow: "+str(t_slow)+" s")
