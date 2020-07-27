import numpy as np
import matplotlib.pyplot as plt

n = 80 # Dimensione massima della matrice
xdim = np.arange(1, n + 1)
y = np.zeros(n) # Array contenente gli errori di ogni matrice
z = np.zeros(n) # Array contenente il numero di condizione di ogni matrice

# Calcolo dei risultati
# Ogni iterazione corrisponde alla risoluzione di un sistema di equazioni #lineari di ordine d
for dim in range(1, n + 1):
    # Costruzione matrice di Vandermonde
    c = np.array([i+1 for i in range(dim)])
    A = np.array([[float(c[j]) ** i for j in range(dim)] for i in range(dim)])
    # Costruzione soluzione
    xsol = np.ones((dim,1))
    # Costruzione vettore termini noti
    b = np.dot(A, xsol)
    # Calcolo soluzione numerica
    x = np.linalg.solve(A,b)
    # Calcolo numero di condizione di A e dell'errore
    z[dim - 1] = np.linalg.cond(A)
    y[dim - 1] = np.linalg.norm(xsol - x) / np.linalg.norm(xsol)

# Costruzione del grafico
plt.title("Crescita dell'errore al crescere della dimensione della matrice\n")
plt.xlabel('Dimensione della matrice')
plt.ylabel('Errore')
plt.yscale('log')
plt.plot(xdim, y, '-g', label = 'Errore calcolato')
plt.plot(xdim, z, '--', label = 'Numero di condizione')
plt.legend()
plt.show()