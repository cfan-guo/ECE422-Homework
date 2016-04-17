#ps 12
import math

# Question 2
g1 = 10**-0.06
g2 = 10**1.2
g3 = 10**-0.08
L1 = 10**0.06
L2 = 10**0.08
L3 = 10**0.48
t0 = 290
#tcas = (L1-1)*t0+70/(g1)+((L2-1)*t0)/(g1*g2)+((L3-1)*t0)/(g1*g2*g3)
tcas = 181.62
print(tcas)

Ta = 25
SNRo = 10**1.721 # given
SNRi = (1+tcas/Ta)*SNRo
print("SNRi: "+str(SNRi))

B = 100*10**6 # 100MHz
k = 1.38064852*10**-23 # Boltzmann Const
Wr = SNRi*k*Ta*B # power at input
print("Wr: "+str(Wr*10**12)+"pW") 

Twla = (L1-1)*t0+70/(g1) # Teff of waveguide, LNA
Gwla = g1*g2 # gain of waveguide, LNA
Psig = Wr*Gwla # signal power at A
N = Gwla*k*Twla*B #noise at A
print("Teff wg, LNA: "+str(Twla))
print("Gain wg, LNA: "+str(Gwla))
print("Psig@A: "+str(Psig*10**12)+"pW")
print("Noise@A: "+str(N*10**12)+"pW")

Pa = (Psig+N)
print("Power@A: "+str(Pa*10**12)+"pW")
