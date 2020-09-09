import numpy as np
import matplotlib.pyplot as plt

# Definizione funzione da integrare
def f(x):
    y = x
    return y

def F(x):
    y = (x**2)/2
    return y

#Calcolo formula del Trapezio
def Trapezi(f,a,b):
    #formula di quadratura
    T = (f(a) + f(b))*(b-a)/2
    return T

# Intervallo di integrazione
a = 2.0 ; b = 6.0

# Calcolo valore esatto integrale
I = F(b) - F(a)

# Calcolo integrale ed errore
T = Trapezi(f,a,b)

E = abs(I - T)
print('Integrale esatto : %f' % I)
print('Formula del Trapezio : %f' % T)
print('Errore commesso : %e' % E)

# Rappresentazione grafica
x = np.linspace(a-0.1,b+0.1,200)
y = f(x)
plt.figure(1)
plt.plot(x,y,label='f(x)',linewidth=1.2)
xx = np.array([a,a,b,b,a])
yy = np.array([0,f(a),f(b),0,0])
plt.plot(xx,yy)
plt.xlabel('x')
plt.ylabel('y')
plt.show()