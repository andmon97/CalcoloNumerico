import numpy as np
from random import random
import math
n = 9
# Costruzione matrice test (composta da numeri casuali tra 1 e 10)
A = np.array([[float(math.ceil(random()*10)) for j in range(n)] for i in range(n)])
# Costruzione soluzione del problema test (vettore formato da numeri che vanno da 1 a n)
xsol = np.ones((n,1))
# Costruzione vettore termini noti
b = np.dot(A,xsol)
print('\nSistema di equazioni lineari Ax = b: \n')
for i in range (n):
    for j in range (n):
        print('%2d*x%d ' %(A[i,j],j+1), end = " ")
        if j != (n-1):
            print('+', end = " ")
        else:
            print(' = %d\n' %b[i])
# Calcolo soluzione del sistema di equalzioni lineari
xt = np.linalg.solve(A,b)
print("\nSoluzione del sistema ipotizzata:")
for i in range (n):
    print("%.15f" %xsol[i])
print("\nSoluzione del sistema calcolata:")
for i in range (n):
    print("%.15f" %xt[i])
# Calcolo numero di condizione di A (ottenuto dal teorema del condizionamento)
K = np.linalg.cond(A) #K(A) = ||A||*||A^(-1)|| sempre >= 1
#Calcolo dell'errore sulla soluzione del sistema
Ex = np.linalg.norm(xsol-xt)/np.linalg.norm(xsol)
print('\nNumero di condizione di A : %e' % K)
print('Errore soluzione sistema : %e' % Ex)