import numpy as np

def EliminazGauss(A,b):
    A = np.copy(A)
    b = np.copy(b)
    n = len(A)
    for j in range(n-1):
        for i in range(j+1,n):
            m = A[i,j]/A[j,j]
            A[i,j] = 0
            for k in range(j+1,n):
                A[i,k] = A[i,k] - m*A[j,k]
            b[i] = b[i] - m*b[j]
    return A, b


def SostIndietro(A,b):
    n = len(A)
    x = np.zeros(n)
    #controlla se il determinante è != 0
    if abs(np.prod(np.diag(A))) > 1.0e-14:
        for i in range(n-1,-1,-1):
            S = 0
            for j in range(i+1,n):
                S = S + A[i,j]*x[j]
            x[i] = (b[i] - S)/A[i,i]
    else:
        print('Errore: matrice singolare o mal condizionata')
        return [] #restituisce un vettore vuoto per segnalare che det != 0
    return x

import numpy as np
from random import random
import math

# Costruzione matrice (composta da numeri casuali tra 1 e 10)
n = 5
A = np.array([[float(math.ceil(random()*10)) for j in range(n)] for i in range(n)])
xsol = np.ones((n,1))
b = np.dot(A,xsol)
# Stampa del sistema
print('\nSistema di equazioni lineari Ax = b: \n')
for i in range (n):
    for j in range (n):
        print('%5.2f*x%d ' %(A[i,j],j+1), end = " ")
        if j != (n-1):
            print('+', end = " ")
        else:
            print(' = %2.2f\n' %b[i])

# Risoluzione del sistema
U, c = EliminazGauss(A,b)

# Stampa del sistema equivalente
print('\nSistema equivalente ottenuto con l\'algoritmo di Gauss senza pivoting: \n')
for i in range (n):
    for j in range (n):
            print('%6.2f*x%d ' %(U[i,j],j+1), end = " ")
            if j != (n-1):
                print('+', end = " ")
            else:
                print(' = %3.2f\n' %c[i])
    xt = SostIndietro(U,c)
if len(xt) > 0:
    print("\nSoluzione del sistema ipotizzata:")
    for i in range (n):
        print("%.20f" %xsol[i])
    print("\nSoluzione del sistema calcolata:")
    for i in range (n):
        print("%.20f" %xt[i])
    err = np.linalg.norm(xt-xsol)/np.linalg.norm(xsol)
    print('\nErrore in soluzione sistema: % e' % err)