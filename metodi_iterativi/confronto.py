import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import time


def GaussSeidel(A,b,x0,tol,Kmax):
    # Dimensione del problma
    n = len(A)
    # Inizializzare il ciclo di calcolo
    k = 0;
    stop = False
    x1 = np.zeros(n)
    while not (stop) and k < Kmax:
        for i in range(n):
            S = 0
            for j in range(0, i):
                S = S + A[i, j] * x1[j]
            for j in range(i + 1, n):
                S = S + A[i, j] * x0[j]
            x1[i] = (b[i] - S) / A[i, i]

        # Controllo della convergenza
        res_rel = la.norm(b - np.dot(A, x1)) / la.norm(b)
        diff_rel = la.norm(x1 - x0) / la.norm(x1)
        stop = (res_rel < tol) and (diff_rel < tol)
        k = k + 1
        x0 = np.copy(x1);

    if not (stop):
        print('Processo non converge in %d iterazioni' % Kmax)
    return x1, k

def Jacobi(A, b, x0, tol, Kmax):
    # Dimensione del problma
    n = len(A)
    # Inizializzare il ciclo di calcolo
    k = 0
    stop = False
    x1 = np.zeros(n)

    while not (stop) and k < Kmax:
        # calcolo di una nuova approssimazione
        for i in range(n):
            S = 0
            for j in range(0, n):
                if j == i: continue
                S = S + A[i, j] * x0[j]
            x1[i] = (b[i] - S) / A[i, i]
        # Controllo della convergenza
        res_rel = la.norm(b - np.dot(A, x1)) / la.norm(b)
        diff_rel = la.norm(x1 - x0) / la.norm(x1)

        stop = (res_rel < tol) and (diff_rel < tol)
        k = k + 1

        x0 = np.copy(x1)

    if not (stop):
        print('Processo non converge in %d iterazioni' % Kmax)
    return x1, k


def EGP(A,b):
    A = np.copy(A) ; b = np.copy(b)
    n = len(A)

    # Pivoting
    for j in range(n - 1):
        # Individuazioone del pivot
        amax = abs(A[j][j])
        imax = j

        for i in range(j + 1, n):
            if abs(A[i][j]) > amax:
                amax = abs(A[i][j])
                imax = i

        # Controllo sull'individuazione del pivot
        if amax < 1.0e-15 :
            print("Matrice singolare o mal condizionata")
            return

        # Scambio di riga
        if imax > j :
            for k in range(j, n):
                A[j][k], A[imax][k] = A[imax][k], A[j][k]
            b[j][0], b[imax][0] = b[imax][0], b[j][0]

        # Eliminazione di Gauss sulla colonna j
        for i in range(j+1, n):
            m = A[i][j] / A[j][j]
            A[i][j] = 0
            for k in range(j + 1, n):
                A[i][k] = A[i][k] - m * A[j][k]
            b[i][0] = b[i][0] - m * b[j][0]

    x = SostIndietro(A, b)
    return x

def SostIndietro(A,b):
    n = len(A)
    x = np.zeros((n,1))
    if abs(np.prod(np.diag(A))) > 1.0e-14:
        for i in range(n-1,-1,-1):
            S = 0
            for j in range(i+1,n):
                S = S + A[i][j]*x[j][0]
            x[i][0] = (b[i][0] - S)/A[i][i]
    else:
        print('Errore: matrice singolare o mal condizionata')
    return x


def FattLUP(A,b):
    A = np.copy(A)
    b = np.copy(b)
    n = len(A)

    for j in range(n - 1):  # scelta elemento pivot
        am = abs(A[j][j]); p = j
        for i in range(j + 1, n):
            if abs(A[i][j]) > am:
                am = abs(A[i][j]); p = j

        # eventuale scambio di riga
        if p > j:
            for k in range(n):
                A[j][k], A[p][k] = A[p][k], A[j][k]
            b[j], b[p] = b[p], b[j]

        # Fattorizzazzione
        for i in range(j + 1, n):
            A[i][j] = A[i][j] / A[j][j]
            for k in range(j + 1, n):
                A[i][k] = A[i][k] - A[i][j] * A[j][k]

        y = SostAvanti(A, b)
        x = SostIndietro(A, y)
        return x


def SostAvanti(A, b):
    n = len(A) # Ordine del sistema
    x = np.zeros((n,1)) # Soluzione del sistema
    if abs(np.prod(np.diag(A))) > 1.0e-14:
        for i in range(n):
            S = 0
            for j in range(0, i):
                S += A[i][j] * x[j][0]
            x[i][0] = (b[i][0] - S) / A[i][i]
    else:
        print('Errore: matrice singolare o mal condizionata')
    return x



# Parametri per il metodo
Kmax = 100 ; tol = 1.0e-6 ;
n_vett = range(100,400,50)
#Statistiche Gauss Seidel
Iter_GS = np.zeros(len(n_vett))
Tempo_GS = np.zeros(len(n_vett))
#Statistiche Jacobi
Iter_J = np.zeros(len(n_vett))
Tempo_J = np.zeros(len(n_vett))
#Statistiche Eliminazione Gauss con Pivoting
Tempo_EGP = np.zeros(len(n_vett))
#Statistiche Fattorizzazione LU con Pivoting
Tempo_FattLUP = np.zeros(len(n_vett))
i = 0 ;

for n in n_vett:

    # Costurzione problema test di dimensione n
    c = 4
    e1 = np.ones(n-1)
    A = np.diag(e1,-1) - c*np.eye(n) + np.diag(e1,1)
    xsol = np.ones(n)
    b = np.dot(A,xsol)
    # Approssimazione iniziale
    x0 = 2*np.random.rand(n) - 1

    Ripet = 2
    # GaussSeidel
    inizio = time.time()
    for r in range(Ripet):
        x, k = GaussSeidel(A, b, x0, tol, Kmax)
    fine = time.time()
    tempo = (fine - inizio) / Ripet
    Iter_GS[i] = k
    Tempo_GS[i] = tempo

    # Jacobi
    inizio = time.time()
    for r in range(Ripet):
        x, k = Jacobi(A, b, x0, tol, Kmax)
    fine = time.time()
    tempo = (fine - inizio) / Ripet
    Iter_J[i] = k
    Tempo_J[i] = tempo

    b = np.reshape(b, (n, 1))

    # Eliminazione di Gauss con Pivoting
    inizio = time.time()
    for r in range(Ripet):
        x = EGP(A, b)
    fine = time.time()
    tempo = (fine - inizio) / Ripet
    Tempo_EGP[i] = tempo

    # Fattorizzazione LU con Pivoting
    inizio = time.time()
    for r in range(Ripet):
        x = FattLUP(A, b)
    fine = time.time()
    tempo = (fine - inizio) / Ripet
    Tempo_FattLUP[i] = tempo

    i = i + 1

plt.figure(1)
plt.semilogy(n_vett,Iter_GS,'*', label = 'Gauss-Seidel')
plt.semilogy(n_vett,Iter_J,'*', label='Jacobi')
plt.xlabel('n') ; plt.ylabel('Numero Iterazioni')
plt.legend()
plt.figure(2)
plt.semilogy(n_vett,Tempo_GS, label='Gauss-Seidel')
plt.semilogy(n_vett,Tempo_J, label='Jacobi')
plt.semilogy(n_vett,Tempo_EGP, label='EGP')
plt.semilogy(n_vett,Tempo_FattLUP, label='FattLUP')
plt.xlabel('n') ; plt.ylabel('Tempo esecuzione')
plt.legend()
