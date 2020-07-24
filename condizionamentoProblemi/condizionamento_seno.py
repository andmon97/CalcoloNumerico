# Verifica condizionamento della funzione sin(x)
#Inserimento dati
x = float(input('Inserire x: '))
perturb = float(input('Inserire perturbazione : ')) #es. 1.0e-5

# Costruzione dati perturbati
from random import random
xt = x*(1 + perturb*(-1+2*random))

#Calcolo del seno
import math
S = math.sin(x) #sin corretto
St = math.sin(xt) #sin perturbato

# Calcolo degli errori relativi
Ex = abs(x-xt)/abs(x)
ES = abs(S-St)/abs(S)

# Visualizzazione dei risultati
print('Dati esatti x=%15.15f' % x)
print('Dati perturb x=%15.15f' % xt)
print('Sin dato esatto S=%15.15f' % S)
print('Sin dato perturb S=%15.15f' % St)
print('Errore sui dati Ex=%e' % Ex)
print('Errore sul risultato Es=%e' % ES)
if abs((abs(x/math.tan(x))*Ex))<=Ex:
    print('Il sin della x scelta è BENCONDIZIONATO')
else :
    print('Il sin della x scelta è MALCONDIZIONATO')