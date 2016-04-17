# Question 5
from math import *

f = 12.5e9
EIRP_dB = 57 #dBW
EIRP = 10*10**5.7
R = 38548e3 #meters
B = 50e6 
SNR_reqdB = 10
SNR_req = 10e1
T_sys = 600 #k
er = 0.55
M_reqdB = 5.9 #link margin
#FSL only loss

# What is the minimum diameter of a circular dish antenna?
lambda_d = 3e8/f
FSL_dB = 20*log((4*pi*R/lambda_d),10)
#CNR_req = EIRP_dB - FSL_dB + 10*log(Gr/T_sys, 10) + 228.6 - 10*log(B, 10) - M_reqdB
GTrat_dB = SNR_reqdB - EIRP_dB + FSL_dB - 228.6 + 10*log(B, 10) + M_reqdB
GTrat_div10 = GTrat_dB/10
GTrat = 10**GTrat_div10
Gr = GTrat*T_sys # G = G/T*T

#print(GTrat_dB)
#print(GTrat_div10)
print("G/T: "+str(GTrat_dB)+" [dB/K]")
#print(Gr)


#Gr = (L*pi/lambda)^2*er ==> L = sqrt(Gr/er)*lambda/pi
A_phys = Gr/(4*pi*er)*(lambda_d)*(lambda_d)
L1 = (lambda_d/pi)*sqrt(Gr/er)
print("A_phys: "+str(A_phys)+"m^2")
print("Length: "+str(L1)+"m")

