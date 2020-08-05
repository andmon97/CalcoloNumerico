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