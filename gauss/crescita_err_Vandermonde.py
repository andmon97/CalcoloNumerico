import numpy as np

def EliminazGaussConPivoting(A,b):
    A = np.copy(A) ; b = np.copy(b)
    n = len(A)

    for j in range(n-1):
        #individuazione elemento pivot
        amax = abs(A[j,j])
        imax = j
        for i in range(j+1,n):
            if abs(A[i,j]) > amax:
                amax = abs(A[i,j])
                imax = i

        #eventuale scambio di riga
        if imax > j:
            for k in range (j,n):
                A[j,k], A[imax,k] = A[imax,k], A[j,k] #scambio
            b[j], b[imax] = b[imax], b[j]

         #eliminazione di Gauss sulla colonna j
        for i in range(j+1,n):
            m = A[i,j]/A[j,j]
            A[i,j] = 0
            for k in range(j+1,n):
                A[i,k] = A[i,k] - m*A[j,k]
            b[i] = b[i] - m*b[j]

    return A, b


def SostIndietro(A,b):
    n = len(A)
    x = np.zeros(n)
    #controlla se il determinante è != 0
    if abs(np.prod(np.diag(A))) > 1.0e-14:
        for i in range(n-1,-1,-1):
            S = 0
            for j in range(i+1,n):
                S = S + A[i,j]*x[j]
            x[i] = (b[i] - S)/A[i,i]
    else:
        print('Errore: matrice singolare o mal condizionata')
        return [] #restituisce un vettore vuoto per segnalare che det != 0
    return x


#funzione che riceve come parametro il vettore [1,n] di grandezze di matrici e calcola
# l'errore del sistema di eq. lin.
def erroreSistemaEqLin(x):
    Ex = np.zeros(x.size) #inizializzo un vettore di errori di n elementi
    #effettuiamo il calcolo dell'errore per le matrici di dimensione da 1 a x.size
    for n in range(1,x.size+1):
        # Costruzione vettore c per la matrice di Vandermonde in [1,n]
        c = np.array([i+1 for i in range(n)] )

        # Costruzione matrice di Vandermonde (c[j]^i)
        A = np.array([[ float (c[j])**i for j in range(n)] for i in range(n)])

        # Costruzione soluzione del problema test (vettore formato da tutti 1)
        xsol = np.ones((n,1))

        # Costruzione vettore termini noti
        b = np.dot(A,xsol)

        # Risoluzione del sistema
        U, c = EliminazGaussConPivoting(A,b)
        xt = SostIndietro(U,c)

        #Calcolo dell'errore sulla soluzione del sistema
        Ex[n-1] = np.linalg.norm(xsol-xt)/np.linalg.norm(xsol)
    return Ex

import numpy as np
import matplotlib.pyplot as plt
n = 100
x = np.arange(1, n)
y = erroreSistemaEqLin(x)
plt.title("Crescita dell'errore al crescere della dimensione della matrice\n")

plt.semilogy(x, y)
plt.xlabel('Dimensione matrice')
plt.ylabel('Errore')
plt.show()

