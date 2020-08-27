import numpy as np
import matplotlib.pyplot as plt

# Dati del problema
x0 = 0 ; xm = 4 ; # Intervallo dei valori
m = 100 # Numero di punti

# Nodi
x = np.linspace(x0,xm,m+1)

# Retta di partenza y=ax+b
b = -1 ; a = 2

# Perturbazione dei punti sulla retta
y = (b + a*x) + (np.random.rand(m+1)-0.5)

# Calcolo della retta di regressione lineare
A = np.zeros((2,2))
d = np.zeros(2)
A[0,0] = m+1
A[0,1] = np.sum(x) ; A[1,0] = A[0,1]
A[1,1] = np.sum(x**2)
d[0] = np.sum(y) ; d[1] = np.sum(x*y)
c = np.linalg.solve(A,d)

# Grafico della retta ricostruita
xg = np.linspace(x0,xm,200)
yg = c[0] + c[1]*xg

# Grafico
plt.figure(0)
plt.plot(xg,yg,label='Retta reg. lin. y=c0+c1x')
plt.plot(x,y,'r+', label='Punti della retta y=ax-b perturbati')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.show(block=False)

# Grafico
plt.figure(1)
plt.plot(xg,a*xg+b,label='Retta originaria: y=ax+b')
plt.plot(xg,yg,label='Retta reg. lin. y=c0+c1x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.show(block=False)