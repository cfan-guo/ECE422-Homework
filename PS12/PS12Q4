#Question 4

from math import *

c = 3e8

CNR_req = 10**(10.5/10.0) #CNR is 10.5dB
B_noise = 36e6 #36MHz
R = 35789e3 #distance in meters

#a) performance of uplink signal
print("Part a)")
f_u = 6.305e9
GTa_ratiodB = -6 #in dB/K
IPBO = 2 #in dB
Pr_satdB = -80 #dB/m^2
Pr_sat = 10**(-80/10.0)

lambda_u = c/f_u
FSL_u = 20*log((4*pi*R/lambda_u),10)
BdB = 10*log(B_noise, 10)

# Pr = EIRP/(4*pi*r^2)
EIRP_u = Pr_sat*(4*pi*R**2)
EIRP_udB = 10*log(EIRP_u, 10)

CN0R_udB = EIRP_udB - IPBO - FSL_u + GTa_ratiodB + 228.6 
print("EIRP uplink: "+str(EIRP_udB))
print("CNR uplink: "+str(CN0R_udB))

#b) performance of downlink signal
print("\nPart b)")
# CNR_req = ((CNR_1)^1+(CNR_2)^-1)^-1
# given as CNR (B specific), so find B specific and then do CN0R

CNR_udB = CN0R_udB-BdB
CNR_u = 10**(CNR_udB/10.0)

CNR_d = (CNR_req**-1 - CNR_u**-1)**-1
CNR_ddB = 10*log(CNR_d, 10)
CN0R_ddB = CNR_ddB+BdB

print("CNR uplink: "+str(CNR_udB))
print("CNR downlink: "+str(CN0R_ddB))

#c) receiving station characteristics
print("\nPart c)")
Wr_satdB = 36 # dBw
f_d = 4.080e9 

lambda_d = c/f_d
FSL_d = 20*log((4*pi*R/lambda_d),10)

# this thing uses the sat - IPBO from a)
Pr_in = (EIRP_u*10**(IPBO/-10.0))/(4*pi*R**2)

# Wout = Wsat*(4*Pin/Psat)/(1+(Pin/Psat))^2
Wr_sat = 10**(Wr_satdB/10.0)
W_out = Wr_sat*(4*Pr_in/Pr_sat)/(1+(Pr_in/Pr_sat))**2

EIRP_d =  W_out
EIRP_ddB = 10*log(EIRP_d, 10)

print("EIRP downlink: "+str(EIRP_ddB))

#d) G/T ratio
print("\nPart d)")
GTc_ratiodB = CN0R_ddB - EIRP_ddB + FSL_d - 228.6 #in dB/K
GTc_ratio = 10**(GTc_ratiodB/10.0)
print("G/T ratio: "+str(GTc_ratiodB)+" [dB/k]")

#e) system noise temp
print("\nPart e)")

Dia = 3.048
Eap = 0.65

G_ant = Eap*(Dia*pi/lambda_d)**2
G_antdB = 10*log(G_ant, 10)

# GTratio = G/T => T = G/GTratio
T_sys = G_ant/GTc_ratio

print("Antenna gain: "+str(G_antdB))
print("T_sys: "+str(T_sys)+" k")

#f) Noise figure for first amplifier
print("\nPart f)")
T_sky = 0.95*5
T_earth = 0.05*290
T_skyy = T_sky + T_earth
T_a = T_skyy

T_eq = 10 # all succeeding stages contribute at input to first amp

T_cas = T_sys - T_skyy
T_amp = T_cas - T_eq
F_amp = (1+T_amp/290)
F_ampdB = 10*log(F_amp, 10)

print("T_a: "+str(T_a)+" k")
print("T_amp: "+str(T_amp)+" k")
print("Noise figure of amp: "+str(F_ampdB)+"[dB]")
