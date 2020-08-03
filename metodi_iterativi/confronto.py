import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import time
from random import random
import math


def GaussSeidel(A,b,x0,tol,Kmax):
    # Dimensione del problma
    n = len(A)

    # Inizializzare il ciclo di calcolo
    k = 0 ; stop = False
    x1 = np.zeros(n)

    while not (stop) and k < Kmax:
        for i in range(n):
            S = 0
            for j in range(0, i):
                S = S + A[i, j] * x1[j]
            for j in range(i + 1, n):
                S = S + A[i, j] * x0[j]
            x1[i] = (b[i] - S) / A[i, i]

        # Controllo della convergenza
        res_rel = la.norm(b - np.dot(A, x1)) / la.norm(b)
        diff_rel = la.norm(x1 - x0) / la.norm(x1)

        stop = (res_rel < tol) and (diff_rel < tol)
        k = k + 1

        x0 = np.copy(x1);

        if not (stop):
            print('Processo non converge in %d iterazioni' % Kmax)
        return x1, k


def Jacobi(A,b,x0,tol,Kmax):
    # Dimensione del problma
    n = len(A)

    # Inizializzare il ciclo di calcolo
    k = 0 ; stop = False
    x1 = np.zeros(n)

    while not (stop) and k < Kmax:
        for i in range(n):
            S = 0
            for j in range(0, i):
                S = S + A[i, j] * x0[j]
            for j in range(i + 1, n):
                S = S + A[i, j] * x0[j]
            x1[i] = (b[i] - S) / A[i, i]
        # Controllo della convergenza
        res_rel = la.norm(b - np.dot(A, x1)) / la.norm(b)
        diff_rel = la.norm(x1 - x0) / la.norm(x1)
        stop = (res_rel < tol) and (diff_rel < tol)
        k = k + 1
        x0 = np.copy(x1);
        if not (stop):
            print('Processo non converge in %d iterazioni' % Kmax)
        return x1, k


def EliminazGauss(A,b):
    A = np.copy(A) ; b = np.copy(b)
    n = len(A)
    for j in range(n-1):
        for i in range(j+1,n):
            m = A[i,j]/A[j,j]
            A[i,j] = 0
            for k in range(j+1,n):
                A[i,k] = A[i,k] - m*A[j,k]
            b[i] = b[i] - m*b[j]
    xt = SostIndietro(A,b)
    return xt


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

def SostAvanti(A,b):
    n = len(A)
    y = np.zeros(n)
    #controlla se il determinante è != 0
    if abs(np.prod(np.diag(A))) > 1.0e-14:
        for i in range(n):
            S = 0
            for j in range(i):
                S = S + A[i,j]*y[j]
            y[i] = (b[i] - S)/A[i,i]
    else:
        print('Errore: matrice singolare o mal condizionata')
        return [] #restituisce un vettore vuoto per segnalare che det != 0
    return y

def FattLU(A,b):
    A = np.copy(A)
    n = len(A)
    L = np.zeros((n,n))
    for j in range(n-1):
        L[j,j] = 1
        for i in range(j+1,n):
            m = A[i,j]/A[j,j]
            A[i,j] = 0
            for k in range(j+1,n):
                A[i,k] = A[i,k] - m*A[j,k]
            L[i,j] = m
    L[n-1,n-1] = 1

    yt = SostAvanti(L,b)
    xt = SostIndietro(A,yt)
    return xt



# Parametri per il metodo
Kmax = 100 ; tol = 1.0e-6 ;
n_vett = range(100,400,50) #vettore formato da [100,150,200,250,300,350]

Iter_GS = np.zeros(len(n_vett)) #vettore del numero di iterazioni di ogni test con Gauss-Seidel
Tempo_GS = np.zeros(len(n_vett)) #vettore del tempo di esecuzione di ogni test con Gauss-Seidel

Iter_J = np.zeros(len(n_vett)) #vettore del numero di iterazioni di ogni test con Jacobi
Tempo_J = np.zeros(len(n_vett)) #vettore del tempo di esecuzione di ogni test con Jacobi

Tempo_EG = np.zeros(len(n_vett)) #vettore del tempo di esecuzione di ogni test con Gauss
Tempo_LU = np.zeros(len(n_vett)) #vettore del tempo di esecuzione di ogni test con fatt LU

i = 0 ;
for n in n_vett:
    # Costurzione problema test con matrice a predominanza diagonale di dimensione n
    c = 6;
    e1 = np.ones(n - 1)
    A = np.diag(e1, -1) - c * np.eye(n) + np.diag(e1, 1)
    xsol = np.ones(n)
    b = np.dot(A, xsol)

    # Approssimazione iniziale: vettore random con valori tra 1 e 10
    x0 = np.array([float(math.ceil(random() * 10)) for i in range(n)])

    Ripet = 2;
    inizio = time.time()
    for r in range(Ripet):
        x, k = GaussSeidel(A, b, x0, tol, Kmax)
    fine = time.time()
    tempo = (fine - inizio) / Ripet  # media tra due tempi per maggior precisione
    Iter_GS[i] = k
    Tempo_GS[i] = tempo

    inizio = time.time()
    for r in range(Ripet):
        x, k = Jacobi(A, b, x0, tol, Kmax)
    fine = time.time()

    tempo = (fine - inizio) / Ripet  # media tra due tempi per maggior precisione
    Iter_J[i] = k
    Tempo_J[i] = tempo

    inizio = time.time()
    for r in range(Ripet):
        x = EliminazGauss(A, b)
    fine = time.time()
    tempo = (fine - inizio) / Ripet  # media tra due tempi per maggior precisione
    Tempo_EG[i] = tempo

    inizio = time.time()
    for r in range(Ripet):
        x = FattLU(A, b)
    fine = time.time()
    tempo = (fine - inizio) / Ripet  # media tra due tempi per maggior precisione
    Tempo_LU[i] = tempo

    i = i +1

plt.figure(1)
plt.plot(n_vett,Iter_GS,'r*', label='Gauss-Seidel')
plt.plot(n_vett,Iter_J,'r*', label='Jacobi')
plt.legend()
plt.xlabel('Dimensione matrice (n)') ; plt.ylabel('Numero Iterazioni')

plt.figure(2)
plt.semilogy(n_vett,Tempo_GS, label='Gauss-Seidel')
plt.semilogy(n_vett,Tempo_J, label='Jacobi')
plt.semilogy(n_vett,Tempo_EG, label='Elim Gauss')
plt.semilogy(n_vett,Tempo_LU, label='Fatt LU')
plt.legend()
plt.xlabel('Dimensione matrice (n)') ; plt.ylabel('Tempo esecuzione')