# question 3

from math import *

k = 1.38064852*10**-23 # Boltzmann Const

f = 6*10**9 #6GHz
B = 1*10**6 #1MHz
T_sky = 20 #20k
L_at = 10**(0.6) #6dB attenuation
L_rain = 10**(0.4) #4dB attenuation
T_at = 200
T_rain = 270
T_o = 290

er = 1 # 100% efficiency
Wr = 10**(-13) #-100dBm received power
F_amp = 10**(0.3) #3dB noise figure amplifier

#a) what is effective antenna temp at input?
T_skyy = T_sky/(L_at*L_rain)+(L_at-1)/(L_at*L_rain)*(T_at)+(L_rain-1)/(L_rain)*(T_rain)
T_a = er*T_skyy+(1-er)*T_o
print("\n Part a")
print("T'sky: "+str(T_skyy))
print("effective antenna temp @ input: "+str(T_a))

#b) what is the SNR at the output of the amplifier?
T_amp = (F_amp-1)*T_o
T_sys = T_a+T_amp
SNRi = Wr/(k*T_a*B)
F_cas = (1+T_amp/T_a)
SNRo = SNRi/F_cas
print("\n Part b")
print("SNR at input: "+str(SNRi))
print("SNR at output: "+str(SNRo))
print("SNR at input [dB]: "+str(10*log(SNRi,10)))
print("SNR at output [dB]: "+str(10*log(SNRo,10)))

#c) what is SNR if the antenna has er=0.7
er = 0.7 # 70% efficiency
T_skyy = T_sky/(L_at*L_rain)+(L_at-1)/(L_at*L_rain)*(T_at)+(L_rain-1)/(L_rain)*(T_rain)
T_a = er*T_skyy+(1-er)*T_o
T_sys = T_a+T_amp
SNRi = Wr/(k*T_a*B)
F_cas = (1+T_amp/T_a)
SNRo = SNRi/F_cas
print("\n Part c")
print("SNR at input: "+str(SNRi))
print("SNR at output: "+str(SNRo))
print("SNR at input [dB]: "+str(10*log(SNRi,10)))
print("SNR at output [dB]: "+str(10*log(SNRo,10)))
