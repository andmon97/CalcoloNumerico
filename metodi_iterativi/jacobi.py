import numpy as np
import numpy.linalg as la
from random import random
import math

def Jacobi(A,b,x0,tol,Kmax,xsol):
    # Dimensione del problma
    n = len(A)

    # Inizializzare il ciclo di calcolo
    k = 0 ; stop = False
    x1 = np.zeros(n)

    err_rel_vett = np.zeros(Kmax)
    residuo = np.zeros(Kmax)
    diff_it_succ = np.zeros(Kmax)

    print('|-----+--------------+--------------+--------------+--------------|')
    print('| k | Errore Rel | Residuo Rel | Diff It Succ | Tol |')
    print('|-----+--------------+--------------+--------------+--------------|')
    while not (stop) and k < Kmax:
        for i in range(n):
            S = 0
        for j in range(0, i):
            S = S + A[i, j] * x0[j]
        for j in range(i + 1, n):
            S = S + A[i, j] * x0[j]
        x1[i] = (b[i] - S) / A[i, i]

        # Controllo della convergenza
        res_rel = la.norm(b - np.dot(A, x1)) / la.norm(b)  # residuo
        diff_rel = la.norm(x1 - x0) / la.norm(x1)  # confronto tra iter. succ.

        stop = (res_rel < tol) and (diff_rel < tol)

        err_rel = la.norm(x1 - xsol) / la.norm(xsol)  # errore effettivo al passo k
        err_rel_vett[k] = err_rel
        residuo[k] = res_rel;
        diff_it_succ[k] = diff_rel;

        k = k + 1

        print('| %3d | %e | %e | %e | %e | ' % (k, err_rel, res_rel, diff_rel, tol))
        x0 = np.copy(x1);

    print('|-----+--------------+--------------+--------------+--------------|')

    if not (stop):
        print('Processo non converge in %d iterazioni' % Kmax)

    return x1, k, err_rel_vett, residuo, diff_it_succ

    # Costurzione del problema test con matrice a predominanza diagonale
    n = 1200;
    c = 10;  # se c è grande la convergenza è piu veloce
    e1 = np.ones(n - 1)
    A = np.diag(e1, -1) - c * np.eye(n) + np.diag(e1, 1)
    xsol = np.ones(n)
    b = np.dot(A, xsol)

    # Parametri per il metodo: vettore di soluzione random con valori tra 1 e 10
    x0 = np.array([float(math.ceil(random() * 10)) for i in range(n)])
    Kmax = 100;
    tol = 1.0e-6;

    x, k, err_rel_vett, residuo, diff_it_succ = Jacobi(A, b, x0, tol, Kmax, xsol)

    import matplotlib.pyplot as plt
    plt.figure(1)

    plt.semilogy(range(k), err_rel_vett[0:k], label='Errore effettivo')
    plt.semilogy(range(k), residuo[0:k], label='Residuo')
    plt.semilogy(range(k), diff_it_succ[0:k], label='Diff. Iter. Succ.')
    plt.semilogy(range(k), np.ones(k) * tol, '--', label='Tolleranza')
    plt.legend()
    plt.xlabel('k')
    plt.ylabel('Errore')