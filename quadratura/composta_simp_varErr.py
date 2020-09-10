import numpy as np
import matplotlib.pyplot as plt

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
    return S

# Intervallo di integrazione
a = 2.0 ; b = 6.0
# Calcolo valore esatto integrale
I = F(b) - F(a)
# Calcolo integrale ed errore
print('Integrale esatto : %f' % I)
N_range = range(1,200,10)
Errore = np.zeros(len(N_range))

for i in range(len(N_range)):
    N = N_range[i]
    T = SimpsonComposta(f,a,b,N)
    Errore[i] = abs(I - T)
    print('N=%d Errore=%e' %(N,Errore[i]))

plt.figure(1)
plt.semilogy(N_range,Errore,label='Errore Simpson')
plt.xlabel('N')
plt.legend()
plt.show()