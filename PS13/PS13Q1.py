# Question 1
from math import *

f = 100e6
r_moon = 1738e3 #m
R_m2earth = 3.844e8 #m

#Part a) what is RCS?
print("\nPart a)")
RCS = pi*(r_moon)**2
print("RCS: "+str(RCS)+" m^2")

#Part b) What is the min Wt?
Wr_dB = -140 #dBW
Wr = 10**(-14)
Dia = 10 # m
Eap = 0.6 # aperture efficiency

wavelen = 3e8/f

# antenna efficiency
Aeff = pi*(Dia/2.0)**2*Eap
Gr = Eap*(pi*Dia/wavelen)**2

# Finding losses
FSL = (4*pi*R_m2earth)**2
FSL_dB = 10*log(FSL,10)

# Wr = EIRP*RCS*Aeff/(4*pi*R^2*l)^2
# Wr = WtGt*RCS*Aeff/(4*pi*R^2*l)^2
# => Wt = (Wr*(4*pi*R^2*l)^2)/(Gt*RCS*Aeff)
Wt = (Wr*(4*pi*(R_m2earth**2))**2)/(Gr*RCS*Aeff)

print("Antenna gain: "+str(Gr))
print("Power min Wt: "+str(Wt))
# CHECK THINGS ABOUT FSL BEING COUNTED IN THE LOSS
