# Question 7
from math import *

R_earth = 6378e3
R_orb = 250e3
R_total = R_earth + R_orb
mu = 3.986e14 # Nm^2/kg

T = (2*pi*(R_total)**(3/2.0))/sqrt(mu)/60 # period in minutes, decimal
T_sec = int((T-int(T))*60)
T_min = int(T)
print("Orbital period: "+str(T_min)+" min "+str(T_sec)+" sec")
v = sqrt(mu/R_total)
print("Velocity: "+str(v*10**-3)+"km/s")
