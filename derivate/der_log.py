# Errore approssimazione derivata prima mediante rapporti incrementali
import matplotlib.pyplot as plt
import numpy as np

# Funzione di cui vogliamo calcolare la derivata
def f( x ):
    fx = np.log(abs(x))
    return fx

# Derivata prima della funzione
def f1( x ):
    f1x = 1/x
    return f1x

# Punto in cui vogliamo calcolare la derivata
x = 20

# Sequenza di passi h in scala logaritmica
#h = np.logspace(-16,-0,100)
h = 2.0**(-np.array(range(60)))
# Calcolo della derivata in maniera esatta
df = f1(x)

errass = np.zeros(len(h))
print(' Derivata Approssimaz. Errore')
for i in range(len(h)):
    # Approssimazione derivata mediante rapporto incrementale
    dfh = (f(x+h[i])-f(x))/h[i]
    # Calcolo dell'errore assoluto
    errass[i] = np.abs(df-dfh)
    print('%10.8f %10.8f %e' % (df,dfh,errass[i]))

# Grafico in scala logaritmica
plt.figure(1)
plt.plot(h,errass,'*-g')
plt.loglog(h,errass,'*-g')
plt.xlabel('h')
plt.ylabel('Error')
plt.show()