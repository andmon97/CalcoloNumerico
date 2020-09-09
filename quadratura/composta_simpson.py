import numpy as np
import matplotlib.pyplot as plt
from interpolazione.lagrange_baricentrica import Lagrange

# Definizione funzione da integrare
def f(x):
    #y = -6*x**2 + 16*x - 4
    y = np.cos(x)+2
    return y

def F(x):
    #y = -2*x**3 + 8*x**2 - 4*x + 2
    y = np.sin(x)+2*x
    return y

# Calcolo formula composta Simpson
def SimpsonComposta(f,a,b,N):
    # Calcolo estremi sottointervallo
    z = np.linspace(a,b,N+1)
    # Calcolo formula di quadratura
    fz = f(z)
    S1 = 0
    for i in range(1,N):
        S1 = S1 + fz[i]

    S2 = 0
    for i in range(0, N):
        med = (z[i] + z[i + 1]) / 2
        S2 = S2 + f(med)

    S = (fz[0] + 2 * S1 + 4 * S2 + fz[N]) * (b - a) / 6 / N

    # Rappresentazione grafica di Simpson
    x_punti = np.linspace(z[0],z[1]-0.1,200)
    x_nodi = np.array([z[0], (z[0] + z[1]) / 2, z[1]])
    y_nodi = np.array([fz[0], f((z[0] + z[1]) / 2), fz[1]])
    p = Lagrange(x_nodi, y_nodi, x_punti)
    x = np.array([z[1], z[1], z[0], z[0]])
    y = np.array([fz[1], 0, 0, fz[0]])
    plt.plot(x_punti, p, 'r:', label='Appross.\nSimpson Composta', linewidth=1.7)
    plt.plot(x, y, 'r:', linewidth=1.7)

    for i in range(1, N):
        x_punti = np.linspace(z[i], z[i + 1] - 0.1, 200)
        x_nodi = [z[i], (z[i] + z[i + 1]) / 2, z[i + 1]]
        y_nodi = [fz[i], f((z[i] + z[i + 1]) / 2), fz[i + 1]]
        p = Lagrange(x_nodi, y_nodi, x_punti)
        x = np.array([z[i + 1], z[i + 1], z[i]])
        y = np.array([fz[i + 1], 0, 0])
        plt.plot(x_punti, p, 'r:', linewidth=1.7)
        plt.plot(x, y, 'r:', linewidth=1.7)

    return S


# Intervallo di integrazione
a = 2 ; b = 6

# Calcolo valore esatto integrale
I = F(b) - F(a)

# Inizializzazione grafica
fig = plt.figure(1)
ax = fig.add_axes([0,0,1,1])
# Calcolo integrale ed errore
N = 5
S = SimpsonComposta(f,a,b,N)
E = abs(I - S)
print('Integrale essatto : %f' % I)
print('Formula composta di Simpson : %f' % S)
print('Errore commesso : %e' % E)
# Rappresentazione grafica
x = np.linspace(a-0.1,b+0.1,200)
y = f(x)
plt.plot(x,y,'b-',label='f(x)',linewidth=1.2)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')