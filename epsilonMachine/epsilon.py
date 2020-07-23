import numpy as np
u = 1.0
while (1+u)>1 :
    eps = u
    u = u/2;
print('Epsilon: %.20f' %eps)
p = 1 - np.log2(eps)
print('Cifre significative binario: %.5f' %p)
q = p * np.log10(2)
print('Cifre significative decimale: %.5f' %q)