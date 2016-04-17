# Question 4
from math import *

c = 3e8
R_earth = 6378e3 # m
mu = 3.986e14 # blargh
k = 1.38064852*10**-23 # Boltzmann Const

f = 10e9
G_dB = 30 #dB
G = 10**(G_dB/10.0)
Wt = 200e3
tau = 1e-6
B = 1e6

wavelen = c/f

# block diagram of radar rx
T_a = 200

# block 1
L_1dB = 10 
L_1 = 10**(L_1dB/10.0)
F_N1dB = 3
F_N1 = 10**(F_N1dB/10.0)

# block 2
F_N2dB = 6
F_N2 = 10**(F_N2dB/10.0)

SNR_outdB = 10
SNR_out = 10**(SNR_outdB/10.0)
print(SNR_out)

#Part a) 
print("Part a) R_max")

RCS = 5

F_sys = F_N1 +L_1*(F_N2-1) # compares with T_sys calculated by Ivan
T_sys = (F_sys-1)*290

# F_sys = SNR_in/SNR_out => SNR_in = SNR_out*F_sys
# Wr = SNR_in*(K*T_a*B) = (SNR_out*F_sys)*(K*T_a*B)

# Wr = F_sy*SNR_out*(k*T_a*B) # original solve
Wr = SNR_out*(k*(T_a+T_sys)*B) # WHY IS THIS WEIRD *** ASK PROF

print("F_sys: "+str(F_sys))
print("T_sys: "+str(T_sys))
print("Wr: "+str(Wr)+" W") # this answer is different from solutions

A_eff = G/(4*pi/wavelen**2) # this checks out with Ivan
R_max = sqrt(sqrt(A_eff*RCS*Wt*G/Wr)/(4*pi)) # diff from solutions
print("A_eff: "+str(A_eff)+" m^2")
print("R_max: "+str(R_max)+" m")

t_r = 2*R_max/c # diff from solns bc of R_max
print("T_r: "+str(t_r)+" s") 

#Part b) 
print("\nPart b)")
# only one can be in the HPBW at once
theta = sqrt(16/G)
print("Theta: "+str(theta)+" rad")

#
R_min = c*tau/2
print("R_min: "+str(R_min)+"m")

