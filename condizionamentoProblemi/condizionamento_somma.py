# Inserimento valori per esperimento
x = float(input('Inserire dato x: '))
y = float(input('Inserire dato y: '))
perturb = float(input('Inserire parturbazione : ')) #es. 1.0e-5

# Costruzione dati perturbati
from random import random
xt = x*(1 + perturb*(-1+2*random()))
yt = y*(1 + perturb*(-1+2*random()))
#nelle parentesi interna avremo un numero [-1.0, 1.0).


# Calcolo delle somme
S = x + y #somma corretta
St = xt + yt #somma perturbata


# Calcolo degli errori relativi
Ex = abs(x-xt)/abs(x)
Ey = abs(y-yt)/abs(y)
ES = abs(S-St)/abs(S)


# Visualizzazione dei risultati
print('Dati esatti x=%15.15f y=%15.15f' % (x,y))
print('Dati perturb x=%15.15f y=%15.15f' % (xt,yt))
print('Somma dati esatti S=%15.15f' % S)
print('Somma dati perturb S=%15.15f' % St)
print('Errori sui dati Ex=%e Ey=%e ' % (Ex,Ey))
print('Errore sul risultato Es=%e' % ES)
if ES>Ex and ES>Ey:
    print('L\'addizione rispetto ai dati inseriti risulta MALCONDIZIONATA')
else:
    print('L\'addizione rispetto ai dati inseriti risulta BENCONDIZIONATA')