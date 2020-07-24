# Inserimento valori per esperimento
x = float(input('Inserire dato x: '))
y = float(input('Inserire dato y: '))
perturb = float(input('Inserire parturbazione : ')) #es. 1.0e-5


# Costruzione dati perturbati
from random import random
xt = x*(1 + perturb*(-1+2*random()))
yt = y*(1 + perturb*(-1+2*random()))
#nelle parentesi interna avremo un numero [-1.0, 1.0).


# Calcolo dei prodotti
P = x * y #prodotto corretto
Pt = xt * yt #prodotto perturbato


# Calcolo degli errori relativi
Ex = abs(x-xt)/abs(x)
Ey = abs(y-yt)/abs(y)
EP = abs(P-Pt)/abs(P) #EP sarà <= Ex + Ey + Ex*Ey (trascurabile)
#Se Ex e Ey sono piccoli, anche EP sarà piccolo, quindi
#il prodotto è sempre BENCONDIZIONATO


# Visualizzazione dei risultati
print('Dati esatti x=%15.12f y=%15.15f' % (x,y))
print('Dati perturb x=%15.12f y=%15.15f' % (xt,yt))
print('Prodotto dati esatti P=%15.15f' % P)
print('Prodotto dati perturb P=%15.15f' % Pt)
print('Errori sui dati Ex=%e Ey=%e ' % (Ex,Ey))
print('Errore sul risultato Ep=%e' % EP)
if EP< (Ex + Ey + Ex*Ey):
    print('Il prodotto è sempre BENCONDIZIONATO')