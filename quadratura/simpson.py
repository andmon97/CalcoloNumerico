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

# Calcolo formula semplice di Simpson
def FormulaSimpson(f,a,b):
    # formula di quadratura
    S = (f(a) + 4*f((a+b)/2) + f(b))*(b-a)/6
    return S

# Intervallo di integrazione
a = 2.0 ; b = 6

# Calcolo valore esatto integrale
I = F(b) - F(a)

# Calcolo integrale ed errore
S = FormulaSimpson(f,a,b)
E = abs(I - S)

print('\nFUNZIONE DA INTEGRARE: f(x) = cos(x)+2 nell intevallo [%.2f, %.2f]' %(a,b) )
print('Integrale esatto : %f' % I)
print('Formula di Simpson : %f' % S)
print('Errore commesso : %e' % E)

x = np.linspace(a-0.1,b+0.1,200)
y = f(x)

#Calcolo del polinomio di secondo grado sui nodi a,(a+b)/2, b usato da Simpson per
# approssimare la f(x) e calcolare l’integrale
x_nodi = [a,(a+b)/2,b]
y_nodi = [f(a),f((a+b)/2),f(b)]
p = Lagrange(x_nodi,y_nodi,x)

# Rappresentazione grafica
plt.figure(1)
plt.plot(x,y,label='f(x)',linewidth=1.8)
plt.plot(x,p, 'r--', label='Appross.\nSimpson')
xx = np.array([b,b,a,a])
yy = np.array([f(b),0,0,f(a)])
plt.plot(xx,yy, 'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.show()