# Question 6
from math import *

f = 12.5e9
R = 45000e3 # in meters
B = 20e6 # Hz
To = 290
er = 0.8

# a) T_a?
print("\nPart a) T_a?")
T_sky = 20
L_atdB = 8
L_at = 10**0.8
T_at = 260

alpha_r = 1 #dB/km
L_eff = 5 # km
T_rain = 275
L_raindB = alpha_r*L_eff # solve for L_rain
L_rain = 10**(L_raindB/10.0)

T_skyy =  T_sky/(L_at*L_rain)+(L_at-1)/(L_at*L_rain)*(T_at)+(L_rain-1)/(L_rain)*(T_rain)
T_a = (1-er)*To+er*T_skyy
print("T'sky temp: "+str(T_skyy)+"K")
print("Antenna temp: "+str(T_a)+"K")


# b) T_r? T_s?
print("\nPart b) T_r, T_sys?")

D_a = 25 #dB

T_1 = 480
G_1dB = 16

L_2dB = 1.5 # dB
T_phys = To
# solve for T_2
T_2 = To*(10**(L_2dB/10.0)-1)

L_3dB = 7
F_3dB = 3
# solve for T_3
T_3 = To*(10**(F_3dB/10.0)-1)


T_r = T_1+T_2/(10**(G_1dB/10.0))+T_3/(10**(G_1dB/10.0)*10**(L_2dB/-10))
T_sys = T_r + T_a
print("T1: "+str(T_1)+"K")
print("T2: "+str(T_2)+"K")
print("T3: "+str(T_3)+"K")
print("Receiver temp: "+str(T_r)+"K")
print("System temp: "+str(T_sys)+"K")

# c) link margin M
print("\nPart c) Link margin?")

Wt = 8000 #W
Dia = 2 #m
Eap = 0.7
CNR_reqdB = 12 #dB

# Find FSL
lambda_d = 3e8/f
FSL_dB = 20*log(4*pi*R/lambda_d, 10)

# sum losses
L_dB = L_raindB + L_atdB

# Find EIRP
Gt = (Dia*pi/lambda_d)**2*Eap
EIRP = Wt*Gt
EIRP_dB = 10*log(EIRP, 10)

# Gr is the directivity of the rx antenna times its efficiency
Gr = 10**(D_a/10.0)*er

M = EIRP_dB - FSL_dB - L_dB + 10*log(Gr/T_sys, 10) + 228.6 - 10*log(B,10) - CNR_reqdB

print("FSL: "+str(FSL_dB)+"[dB]")
print("EIRP: "+str(EIRP_dB)+"[dB]")
print("Loss: "+str(L_dB)+"[dB]")
print("G/T: "+str(10*log(Gr/T_sys, 10))+"[dB]")
print("Link margin: "+str(M)+"[dB]")

