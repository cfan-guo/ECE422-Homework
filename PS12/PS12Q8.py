# Question 8 - alpha does not match solution but everything else does lel
from math import *

R_e = 6378.2e3 # earth radius in m
R_geo = 35786e3
R_eKM = 6378.2
R_geoKM = 35786
R_tot = R_eKM + R_geoKM
f = 20e9 # 20 GHz freq

# Earth coords
L_e = 52 # deg N
l_e = 0 # deg W
L_eRAD = radians(L_e)
l_eRAD = radians(l_e)

# Satellite coords
l_s = -66 # deg E
L_s = 0 # assumed bc not given
l_sRAD = radians(l_s)
L_sRAD = radians(L_s)


psi_rad = acos(cos(L_eRAD)*cos(L_sRAD)*cos(l_sRAD-l_eRAD)+sin(L_eRAD)*sin(L_sRAD))
psi = degrees(psi_rad)
print("Psi: "+str(psi)+" degrees")

# using cosine law to find things
r_KM = sqrt((R_eKM)**2+(R_tot)**2 - 2*(R_eKM)*(R_tot)*cos(psi_rad))
print ("Distance between station, satellite: "+str(r_KM)+" km")

alpha_rad = acos(R_tot/r_KM*sin(psi_rad))
alpha = degrees(alpha_rad)
print("Alpha: "+str(alpha)+" degrees")

lambda_r = 3e8/f
r = r_KM*10**3
FSL = 20*log(4*pi*r/lambda_r, 10)
print("FSL: "+str(FSL)+" [dB]")
