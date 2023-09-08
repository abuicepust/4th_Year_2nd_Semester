# -*- coding: utf-8 -*-
"""Lab_Practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Uf_2lXHh4lUwj4gJtC2n2Yr0hWEF1_VM
"""

''' Problem -11 '''
from math import pow
bits = [3,3,26,8.25]
bandwidth = 270.833*pow(10,3)
print(f"A time slot has {sum(bits,2*58)} bits")
print(f"A. Number of overhead bits per frame is {int(sum(bits)*8)} bits")
print(f"B. Total number of bits per frame{int(sum(bits,2*58)*8)} bits/frame")
print(f"C. Frame rate is {bandwidth /(sum(bits,2*58)*8) } frame/second")
print(f"D. Time duration of a slot {(sum(bits,2*58))/bandwidth /pow(10,-6)} us")
print(f"E. Frame efficiency Eta {(1- (int(sum(bits)*8))/(sum(bits,2*58)*8)) *100} %")

'''Problem -10'''
from math import pow
bandwidth = 270833 # Hz unit
print(f"A. The time duration of a bit Tb is {(1/bandwidth )/pow(10,-6)} us")
print(f"B. The time duration of a slot Tslot is {156.25*((1/bandwidth )/pow(10,-3))} ms")
print(f"C. The time duration of a frame Tf is {(156.25*((1/bandwidth )))*8 / pow(10,-3)} ms")
print(f"D. A single user has to wait 4.61 ms. The arrival time of new frame for its next transmission ")

'''Problem -09'''
Am,Fm,Ko,Gain = 8,4,10,10    #all parameters ans with Khz so not include 10^3 part
print(f"A. The peak frequency deviation is Deltaf equal to {Am*Gain} Khz")
print(f"B. The modulating index is Betaf equal to {int((Am*Gain)/Fm)}")
print(f"C. The phase modulating index is Betaf equal to  {Am*Ko} radians")

'''Problem -08'''
from math import pow
Pam,k = 400,0.75
''' Solving this task for using equation Pam = Pc(1+(k^2/2))
    then simulation for find Pc = Pam/(1+(k^2/2))'''
Pc = Pam/(1+(pow(k,2)/2))
print(f"A. Percentage of the total power in the carrier is {Pc/Pam *100} % ")
print(f"B. The power in each sideband {(Pam-Pc)*0.5} KW")
print(f"C. The total power saving if the carrier and one of the sidebands are now suppressed {round(((1- ((Pam-Pc)*0.5)/Pam)*100),2)} %")

'''Problem -07'''
from math import pow
N = 70
print(f"A. Delta taw equal to {(150*pow(10,-6) / N)} us  ")
print(f"B. The maximum bandwidth for SIRCIM that can accurately represent equal to {round(2/(150/ N),3)} MHz")
print(f" The maximum bandwidth for SMRCIM that can accurately represent equal to {round(2/(4/ N),3)} MHz")
print(f"C. The indoor channel model for the maximum RF bandwith of for the indoor channel is {2/(500* pow(10,-3) /70)} MHz")

'''Problem -06'''
from math import pow
Fc = 900*pow(10,6)
V = round(70*pow(10,3) /(60*60),2)   # Vehicle speed
lamda = round((3*pow(10,8) / Fc),2)

print(f"A. Toward for the received carrier frequency {(Fc + (V/lamda) )/pow(10,6) } MHz  ")
print(f"B. Away for the received carrier frequency {(Fc- (V/lamda))/pow(10,6)} MHz  ")
print(f"C. The vehicle moving direction to perpendicular so the Theta is 90 degree so that cosine theta is 0,\n So it is same as transmitted frequency {Fc/pow(10,6)} MHz")

'''Problem -05'''
from math import pow,log10,pi
F = 900*pow(10,6)
lamda = round((3*pow(10,8) / F),2)
print(f"A. Fraunhofer distance is Df equal to {int(2*(1*1) / lamda)} m  ")
print(f"B. Path loss PL(db) is equal to {int(-10*log10(pow(lamda/(4*pi*int(2*(1*1) / lamda)),2)))} dB")

'''Problem -04'''
H = round((3/60),2)
lamda = 2
Au = lamda*H
System = ['A','B','C']
C = [19,57,100]
A = [12,45,88]   #obtain from Erlang chart B for each channel and GOS=0.02
cell = [394,98,49]
Resident = 2*pow(10,6)
Combined_subscriber =0;
for i in range(len(System)):
  print(f"For System {System[i]}")
  print(f"User per cell {A[i]/Au}")
  print(f"Total subcriber supported for System {System[i]} is: {cell[i]*(A[i]/Au)}")
  Combined_subscriber+=((cell[i]*(A[i]/Au)))
  print(f"Market penetration for System {System[i]} is: {(cell[i]*(A[i]/Au))/Resident *100} %")
  print(f"Market penetration for combined three system is : {round((Combined_subscriber/Resident)*100 ,2)}%")

'''Problem -03'''
Au = 0.1
Solution = ['a','b','c','d','e']
C = [1,5,10,20,100]
A = [0.005,1.13,3.96,11.10,80.9]   #obtain from Erlang chart B for each channel and GOS=0.005
for i in range(len(Solution)):
  print(f"{Solution[i]}. For trunked channel {C[i]} Total number of users {round(A[i]/Au , 2)} users")

'''Problem -02'''
from math import sqrt,pow,log10
n=[4,3] # path loss component
io = 6 # co channel
'''Equation for reuse factor Q = sqrt(3N) and S/I = (Q)^n / io'''
min_db = 15
N = [7,12]  #cluster size predefined
for i in range(len(N)):
  for j in range(len(n)):
    RF = round(sqrt(3*N[i]),2)
    SI = pow(RF,n[j])/io
    SIdB = round(10*log10(SI),2)
    if(min_db <=SIdB):
      print(f"For {n[j]} Calculate SI is greater than minimum required SI so cluster size {N[i]} can be used")
    else:
      print(f"For {n[j]} Calculate SI is less than minimum required SI so cluster size {N[i]} can't be used. So N need to larger")


'''Problem -01'''
##Lab-1

import math
Total_BW = 30000     
Channel_BW = 25*2
Total_Available_Channel = Total_BW/Channel_BW
Allocated_Spectrum = 1000
Available_Control_Channel = Allocated_Spectrum/Channel_BW
N = [4, 7, 12]
for i in N:   
    Channel_per_cell = Total_Available_Channel / i
    voice_channel_per_cell = (Total_Available_Channel - Available_Control_Channel)/i
    control_channel_per_cell = Channel_per_cell - voice_channel_per_cell
    #print('For',i,'cell reuse pattern: \nTotal number of channels per cell: ',math.floor(Channel_per_cell), '\nVoice channel per cell: ',math.floor(voice_channel_per_cell), '\nControl channel per cell: ', math.ceil(control_channel_per_cell))
    print(f"For {i} cell reuse pattern: \nTotal number of channels per cell: {math.floor(Channel_per_cell)}\nVoice channel per cell: {math.floor(voice_channel_per_cell)}\nControl channel per cell: {math.ceil(control_channel_per_cell)}")