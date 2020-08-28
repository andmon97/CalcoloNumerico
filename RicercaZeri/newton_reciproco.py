from itertools import count
from math import sin, cos

import numpy as np
import matplotlib.pyplot as plt

def Newton(x0, tol, kmax):
    #inizializzazione processo calcolo
    fx0 = fun(x0);
    dfx0 = dfun(x0)
    k = 0;
    stop = False
    valore_f = np.zeros(kmax)
    diff_it_succ = np.zeros(kmax)
    print('|-----+--------------+--------------+--------------+--------------+--------------| ')
    print('|  k  |      x0      |    fun(x0)   | Val Funz     | Diff It Succ |      Tol     | ')
    print('|-----+--------------+--------------+--------------+--------------+--------------| ')

    # ciclo di calcolo
    while not (stop) and k < kmax:
        x1 = x0 - fx0 / dfx0
        fx1 = fun(x1)
        val_fun = abs(fx1) * 5
        iter_succ = abs(x1 - x0) * 5
        stop = (val_fun + iter_succ) < tol
        print('| %3d | %3.10f | %3.10f | %e | %e | %e |'
              % (k, x0, fx0, val_fun, iter_succ, tol))

        valore_f[k] = val_fun
        diff_it_succ[k] = iter_succ

        k = k + 1
        if not (stop):
            x0 = x1;
            fx0 = fx1;
            dfx0 = dfun(x0)

        #verifica convergenza
    if not(stop):
        print('Processo iterativo non converge in %d iterazioni' %kmax)

    return x1, k, valore_f, diff_it_succ


def fun(x):
    y = 2 - 1/x
    return y

def dfun(x):
    y = 1/(x**2)
    return y


x0 = 0.9;
kmax = 100 ; tol = 1.0e-6 ;
xsol, k, val_fun, it_succ = Newton(x0, tol, kmax)
print('La radice ottenuta col metodo di Newton partendo da x0=%.2f affinche 2-1x=0 (1/2)è x=%.5f' %(x0,xsol))
plt.figure(1)
plt.semilogy(range(k),val_fun[0:k],label='Valore funzione')
plt.semilogy(range(k),it_succ[0:k],label='Diff. Iter. Succ.')
plt.semilogy(range(k),np.ones(k)*tol,'--', label='Tolleranza')
plt.legend()
plt.xlabel('k')
plt.ylabel('Errore')
plt.show()