# Verifica condizionamento della funzione sqrt(x)

#Inserimento dati
x = float(input('Inserire x: '))
perturb = float(input('Inserire parturbazione : ')) #es. 1.0e-5

# Costruzione dati perturbati
from random import random
xt = x*(1 + perturb*(-1+2*random()))

#Calcolo della radice quadrata
import math
R = math.sqrt(x) #radice corretta
Rt = math.sqrt(xt) #radice perturbata

# Calcolo degli errori relativi
Ex = abs(x-xt)/abs(x)
ER = abs(R-Rt)/abs(R) #ER sarà approssimato a 1/2 * Ex
#Se Ex è piccolo, anche ER sarà piccolo, quindi
#la radice quadrata è sempre BENCONDIZIONATA


# Visualizzazione dei risultati
print('Dati esatti x=%15.15f' % x)
print('Dati perturb x=%15.15f' % xt)
print('Radice quadrata dato esatto R=%15.15f' % R)
print('Radice quadrata dato perturb Rt=%15.15f' % Rt)
print('Errori sui dati Ex=%e' % Ex)
print('Errore sul risultato Er=%e' % ER)
if (1/2)*Ex<=Ex:
    print('La radice quadrata è sempre BENCONDIZIONATA')