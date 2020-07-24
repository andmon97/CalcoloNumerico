print("Esempio 1")
a = 3.0e-16
b = 1.0
r1 = -1+(b+a)
r2 = (-1+b)+a
r3 = (-1 + (b + a)) / a
print("Operazione 1: -1 + (b + a) = %52.51f" % r1)
print("Operazione 1: (-1 + b) + a = %52.51f" % r2)
print("Operazione 1: (-1 + (b + a)) / a = %52.51f" % r3)
print("Esempio 2")
a = 2e-51
r1 = -1 + (b + a)
r2 = (-1 + b) + a
r3 = (-1 + (b + a)) / a
print("Operazione 1: -1 + (b + a) = %52.51f" % r1)
print("Operazione 1: (-1 + b) + a = %52.51f" % r2)
print("Operazione 1: (-1 + (b + a)) / a = %52.51f" % r3)