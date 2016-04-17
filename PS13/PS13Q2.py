# Question 2
from math import *

R_earth = 6378e3 # m
mu = 3.986e14 # blargh

T_balloon_min = 93.54 # Balloon Period in minutes
A_balloon = 250e3 # Balloon altitude in m
Dia_balloon = 30 # m
f_radar = 10e9 # tracked with 10GHz radar 

RCS = pi*(Dia_balloon/2)**2
wavelen = 3e8/f_radar

# Part a) maximum range to the balloon if atmospheric refraction is ignored
# min useable elev angle is 0 deg
print("\nPart a)")
R_tot = R_earth+A_balloon
range = sqrt(R_tot**2-R_earth**2)
print("Max range: "+str(range)+"m")

# Part b) Max expected doppler shift
print("\nPart b)")
T_balloon_sec = T_balloon_min*60
v_orb = (2*pi*R_tot)/(T_balloon_min*60)
sin_theta = R_earth/R_tot
v_d = v_orb*sin_theta # draw this into some geometry thing, v_d is component of V_orb
delta_f = -2*f_radar*v_d/3e8 # 3e8 is c
print("Orbital velocity: "+str(v_orb)+"m/s")
print("Doppler velocity: "+str(v_d)+"m/s")
print("Doppler shift: "+str(delta_f)+"Hz")

# Part c) Equivalent flat plate area
print("\nPart c)")
A_phys = sqrt(RCS*wavelen**2/(4*pi))
print("Equiv flat plane area: "+str(A_phys)+"m^2")

# Part d) 
print("\nPart d)")
Dia_ant = 5 #m
Eap = 0.55
Wr_dB = -130 # dBW
Wr = 10**(-130/10.0)

# antenna gain
A_eff = pi*(Dia_ant/2.0)**2*Eap
G = Eap*(pi*Dia_ant/wavelen)**2

Wt = Wr*(4*pi*(range**2))**2/(A_eff*G*RCS)
Wt_dB = 10*log(Wt, 10)
print("Antenna effective area: "+str(A_eff)+" m^2")
print("Antenna gain: "+str(G))
print("Power min Wt: "+str(Wt)+"W")
print("Power min Wt: "+str(Wt_dB)+"[dBW]")

# Part e)
print("\nPart e)")
R_rain = 150 #mm/hr
L_eff = 3 #km
k = 0.01
alpha_rain = 1.2

# find rain things a = kR^alpha [dB/km]
a_rain = k*R_rain**alpha_rain
A_rain = a_rain*L_eff
Wt_rain = Wt*(10**(A_rain/10))**2
Wt_raindB = 10*log(Wt_rain,10)

print("Rain attenuation: "+str(A_rain)+"[dB]")
print("New min power: "+str(Wt_rain)+"W")
print("New min power: "+str(Wt_raindB)+"[dBW]")
