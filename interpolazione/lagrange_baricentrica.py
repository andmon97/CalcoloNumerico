import numpy as np
import matplotlib.pyplot as plt

def z_coeff(x_nodi,y_nodi):
    n = len(x_nodi)
    x = np.ones((n,n))
    for i in range(n):
        for j in range(n):
            if j > i:
                x[i,j] = x_nodi[i] - x_nodi[j]
            elif j < i:
                x[i,j] = -x[j,i]
    z = np.zeros(n)
    for j in range(n):
        z[j] = y_nodi[j]/np.prod(x[j,:])
    return z

def calc_Lagrange(x_nodi,z,x):
    n = len(x_nodi)
    pin = np.prod(x-x_nodi)
    S = 0
    for j in range(n):
        S = S + z[j]/(x-x_nodi[j])
    p = pin * S
    return p

def Lagrange(x_nodi,y_nodi,x):
    z = z_coeff(x_nodi,y_nodi)
    m = len(x)
    p = np.zeros(m)
    for i in range(m):
        xx = x[i]
        check_nodi = abs(xx - x_nodi) < 1.0e-14
        if True in check_nodi:
            temp = np.where(check_nodi == True)
            i_nodo = temp[0][0]
            p[i_nodo] = y_nodi[i_nodo]
        else:
            p[i] = calc_Lagrange(x_nodi,z,xx)
    return p

# Funzione da interpolare
def funz(x):
    y = x**4 - 3**2
    return y

# Grado del polinomio di interpolazione
n = 4
# Calcolo dei nodi e dei valori associati
a = -5.00 ; b = 5.00
x_nodi = np.linspace(a,b,n+1)
y_nodi = funz(x_nodi)
# Punti in cui calcolare il polinomio
x = np.linspace(a,b,200)

# Calcolo del polinomio e della funzione
p = Lagrange(x_nodi,y_nodi,x)
f = funz(x)

# Grafico del polinomio di interpolazione
plt.figure(0)
plt.plot(x,p,label='p(x)')
plt.plot(x,f,label='f(x)')
plt.plot(x_nodi,y_nodi,'k*')
plt.legend()
plt.xlabel('x')
plt.title('Pol. interp. grado n=%d di f(x)=x**4 - 3**2in [%4.2f, %4.2f]' % (n,a,b))
plt.show(block=False)

# Grafico del resto del polinomio di interpolazione
plt.figure(1)
plt.semilogy(x,abs(p-f),label='R(x)')
plt.legend()
plt.xlabel('x')
plt.title('Resto pol. interp. grado n=%d di f(x)=x**4 - 3**2  in [%4.2f, %4.2f]' % (n,a,b))
plt.show(block=False)