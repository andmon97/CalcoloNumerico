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

def calc_Newton(x_nodi, d, x):
    n = len(x_nodi)
    p = d[-1]
    for i in range (n-2, -1, -1):
        p = p * (x - x_nodi[i]) + d[i]
    return p

# Funzione da interpolare
def funz(x):
    y = np.sin(x)
    return y

# Grado del polinomio di interpolazione
n = 15
# Calcolo dei nodi e dei valori associati
a = 0 ; b = 2*np.pi
x_nodi = np.linspace(a,b,n+1)
#k = np.array(range(n,-1,-1))
#x_nodi = (a+b)/2 +(b-a)/2*np.cos((2*k+1)*np.pi/2/(n+1))
y_nodi = funz(x_nodi)

# Punti in cui calcolare il polinomio
x = np.linspace(a,b,200)
# Calcolo del polinomio e della funzione
p = Newton(x_nodi, y_nodi, x)
f = funz(x)
# Grafico del polinomio di interpolazione plt.figure(0)
plt.plot(x,p,label='p(x)')
plt.plot(x,f,label='f(x)')
plt.plot(x_nodi,y_nodi,'k*')
plt.legend()
plt.xlabel('x')
plt.title('Pol. interp. grado n=%d di f(x)=sin(x) in [%4.2f %4.2f]' % (n,a,b))
plt.show(block=False)
# Grafico del resto del polinomio di interpolazione
plt.figure(1)
plt.semilogy(x,abs(p-f),label='R(x)')
plt.legend()
plt.xlabel('x')
plt.title('Resto pol. interp. grado n=%d di f(x)=sin(x) in [%4.2f %4.2f]' % (n,a,b))
plt.show(block=False)