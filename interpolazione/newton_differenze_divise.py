import numpy as np
import matplotlib.pyplot as plt

def Newton(x_nodi, y_nodi, x):
    n = len(x)
    p = np.zeros(n)
    d = diffDiv(x_nodi, y_nodi)
    for i in range(n):
        xx = x[i]
        # Se un punto in cui si calcola il polinomio corrisponde
        #ad un nodo: si imposta il valore corrispondente noto
        check_nodi = abs(xx - x_nodi) < 1.0e-14
        if True in check_nodi:
            temp = np.where(check_nodi == True)
            i_nodo = temp[0]
            p[i] = y_nodi[i_nodo]
        else:
            p[i] = calc_Newton(x_nodi, d, xx)
    return p

def diffDiv(x_nodi, y_nodi):
    n = len(x_nodi)
    d = np.copy(y_nodi)
    for j in range (1, n):
        for i in range(n-1, j-1, -1):
            d[i] = (d[i] - d[i-1]) / (x_nodi[i] - x_nodi[i-j])
    return d